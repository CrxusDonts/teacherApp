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
            with transaction.atomic():
                new_user = User.objects.create_user(username=user_name, password=password)
                response_str = 'Class create '
                class_name = register_class(request.data.get('class_name'))
                new_backend_account = BackendAccount.objects.create(user=new_user)
                new_backend_account.save()
                response_str = 'Add manager '
                add_manager(True, new_backend_account, class_name)
        except IntegrityError:
            return Response("User already existed.")
        except Exception:
            return Response(response_str + 'failed.')
        return Response('Register succeed.')

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
                return Response('Modify password failed.')
        else:
            return Response('Old password is not correct.')
        return Response('Modify password succeed.')

    # 登陆
    @action(methods=['post'], detail=False)
    def login(self, request):
        try:
            user_name = request.data.get('user_name')
            password = request.data.get('password')
            user = authenticate(username=user_name, password=password)
            if user:
                login(request, user)
                return Response('Login succeed.')
            else:
                return Response('Login failed.')
        except Exception:
            return Response(status=500)

    # 登出
    @action(methods=['post'], detail=False)
    def logout(self, request):
        try:
            logout(request)
            return Response('logout succeed.')
        except Exception:
            return Response('logout failed.')



class ClassView(viewsets.ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer

    # 添加作业
    @action(methods=['post'], detail=True)
    def new_homework(self, request, pk):
        try:
            clazz = Class.objects.get(id=pk)
        except Exception:
            return Response('Class not found.')
        start_time = request.data.get('start_time')
        due_time = request.data.get('due_time')
        repeatable = request.data.get('repeatable')
        homework = Homework.objects.create(start_time=start_time, due_time=due_time, repeatable=repeatable,
                                           the_clazz=clazz)
        homework.save()
        return Response('New homework succeed.')

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
                    return Response(serializer.data)
        except Exception:
            return Response('Get my own class failed.')

    # 获取我管理的（除了我的班级）班级列表
    @action(methods=['get'], detail=False)
    def get_manage_class_list(self, request):
        try:
            cur_user = request.user
            cur_account = BackendAccount.objects.get(user=cur_user)
            managers = cur_account.account_manager.all()
            class_list = managers.filter(status=1)  # 1代表manager 详细参见models内定义的status
            serializer = ClassSerializer(class_list, many=True)
            return Response(serializer.data)
        except Exception:
            return Response('Get my manage class failed.')


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
            return Response('Homework not found.')
        text_content = request.data.get('text_content')
        choice_question = ChoiceQuestion.objects.create(text_content=text_content, homework=homework)
        choice_question.save()
        return Response('New choice question succeed.')

    # 添加填空题
    @action(methods=['post'], detail=True)
    def new_completion_question(self, request, pk):
        try:
            homework = Homework.objects.get(id=pk)
        except Exception:
            return Response('Homework not found.')
        text_content = request.data.get('text_content')
        completion_question = CompletionQuestion.objects.create(text_content=text_content, homework=homework)
        completion_question.save()
        return Response('New completion question succeed.')


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
