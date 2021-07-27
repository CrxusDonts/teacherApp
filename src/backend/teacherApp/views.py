from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db import transaction
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django.core.serializers import serialize
from rest_framework.utils import json

from .serializers import *


# status 请参考https://www.runoob.com/http/http-status-codes.html

class BackendAccountView(viewsets.ModelViewSet):
    queryset = BackendAccount.objects.all()
    serializer_class = BackendAccountSerializer

    # 注册后台账户
    @action(methods=['post'], detail=False)
    def register_teacher(self, request):
        user_name = request.data.get('user_name')
        password = request.data.get('password')
        try:
            with transaction.atomic():  # 使用with，这样在with下面的代码如果发生错误 自动回滚
                new_user = User.objects.create_user(username=user_name, password=password)
                response_str = 'class create '
                class_name = register_class(request.data.get('class_name'))
                new_backend_account = BackendAccount.objects.create(user=new_user)
                new_backend_account.save()
                response_str = 'add manager'
                add_manager(True, new_backend_account, class_name)
        except IntegrityError:
            return Response("user_name already exists ", status=400)  # 返回bad request 说明user_name已经存在
        except Exception:
            return Response(response_str + 'failed', status=500)
        return Response(status=200)

    # 更改账户的密码
    @action(methods=['put'], detail=False)
    def change_password(self, request):
        old_password = request.data.get('old_password')
        new_password = request.data.get('new_password')
        cur_user = request.user
        if cur_user.check_password(old_password):
            try:
                cur_user.set_password(new_password)
                cur_user.save()
            except Exception:
                return Response(status=500)
        else:
            return Response('authentication failed ', status=400)
        return Response('modify password success', status=200)

    # 登陆
    @action(methods=['post'], detail=False)
    def login(self, request):
        try:
            user_name = request.data.get('user_name')
            password = request.data.get('password')
            user = authenticate(username=user_name, password=password)
            if user:
                # 这里的login是django自带的login，实现用户登录功能
                login(request, user)
                return Response('login successfully', status=200)
            else:
                return Response('login failed ', status=400)  # 返回bad request 说明登录失败
        except Exception:
            return Response(status=500)

    # 登出
    @action(methods=['post'], detail=False)
    def logout(self, request):
        try:
            # 这里的logout是django自带的logout，实现用户登出功能，清除session
            logout(request)
            return Response('logout successfully ', status=200)
        except Exception:
            return Response(status=500)


class ClassView(viewsets.ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer

    # 添加作业
    @action(methods=['post'], detail=True)
    def new_homework(self, request, pk):
        try:
            clazz = Class.objects.get(id=pk)
        except Exception:
            return Response('Class not found', status=404)
        start_time = request.data.get('start_time')
        due_time = request.data.get('due_time')
        repeatable = request.data.get('repeatable')
        homework = Homework.objects.create(start_time=start_time, due_time=due_time, repeatable=repeatable,
                                           the_clazz=clazz)
        homework.save()
        return Response('New homework success', status=200)

    # 获取我的班级
    @action(methods=['get'], detail=False)
    def get_my_class(self, request):
        try:
            cur_user = request.user
            cur_account = BackendAccount.objects.get(user=cur_user)
            managers = cur_account.account_manager.all()
            for manager in managers:
                if manager.get_status_display() == 'owner':
                    serializer = ClassSerializer(manager.class_name)
                    return Response(serializer.data, status=200)
        except Exception:
            return Response(status=500)
        return Response(status=500)

    # 获取我管理的（除了我的班级）班级列表
    @action(methods=['get'], detail=False)
    def get_manage_class_list(self, request):
        try:
            cur_user = request.user
            cur_account = BackendAccount.objects.get(user=cur_user)
            managers = cur_account.account_manager.all()
            class_list = managers.filter(status=1)  # 1代表manager 详细参见models内定义的status
            serializer = ClassSerializer(class_list, many=True)
            return Response(serializer.data, status=200)
        except Exception:
            return Response(status=500)


class ManagerView(viewsets.ModelViewSet):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer


class FrontAccountView(viewsets.ModelViewSet):
    queryset = FrontAccount.objects.all()
    serializer_class = FrontAccountSerializer


class PeopleView(viewsets.ModelViewSet):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer


class ChoiceQuestionView(viewsets.ModelViewSet):
    queryset = ChoiceQuestion.objects.all()
    serializer_class = ChoiceQuestionSerializer


class OptionsView(viewsets.ModelViewSet):
    queryset = Options.objects.all()
    serializer_class = OptionsSerializer


class ChoiceQuestionUserAnswerView(viewsets.ModelViewSet):
    queryset = ChoiceQuestionUserAnswer.objects.all()
    serializer_class = ChoiceQuestionUserAnswerSerializer


class MediaView(viewsets.ModelViewSet):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer


class HomeworkView(viewsets.ModelViewSet):
    queryset = Homework.objects.all()
    serializer_class = HomeworkSerializer

    # 添加选择题
    @action(methods=['post'], detail=True)
    def new_choice_question(self, request, pk):
        try:
            homework = Homework.objects.get(id=pk)
        except Exception:
            return Response('Homework not found', status=404)
        text_content = request.data.get('text_content')
        choice_question = ChoiceQuestion.objects.create(text_content=text_content, homework=homework)
        choice_question.save()
        return Response('New choice_question success', status=200)

    # 添加填空题
    @action(methods=['post'], detail=True)
    def new_completion_question(self, request, pk):
        try:
            homework = Homework.objects.get(id=pk)
        except Exception:
            return Response('Homework not found', status=404)
        text_content = request.data.get('text_content')
        completion_question = CompletionQuestion.objects.create(text_content=text_content, homework=homework)
        completion_question.save()
        return Response('New completion_question success', status=200)


class CompletionQuestionView(viewsets.ModelViewSet):
    queryset = CompletionQuestion.objects.all()
    serializer_class = CompletionQuestionSerializer


class CompletionQuestionAnswerView(viewsets.ModelViewSet):
    queryset = CompletionQuestionAnswer.objects.all()
    serializer_class = CompletionQuestionAnswerSerializer


class CompletionQuestionUserAnswerView(viewsets.ModelViewSet):
    queryset = CompletionQuestionUserAnswer.objects.all()
    serializer_class = CompletionQuestionUserAnswerSerializer


# 用于注册班级的函数
def register_class(name):
    class_name = name
    try:
        new_class = Class.objects.create(class_name=class_name)
        new_class.save()
    except Exception:
        raise Exception
    return new_class


# 用于添加manager表的函数
def add_manager(if_teacher, account, class_name):
    try:
        if_owner = 0 if if_teacher else 1
        new_manager = Manager.objects.create(status=if_owner, account=account, class_name=class_name)
        new_manager.save()
    except Exception:
        raise Exception
