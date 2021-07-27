from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db import transaction
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from .serializers import *


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
                add_manager('True', new_backend_account, class_name)
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
        if_owner = 0 if if_teacher == 'True ' else 1
        new_manager = Manager.objects.create(status=if_owner, account=account, class_name=class_name)
        new_manager.save()
    except Exception:
        raise Exception
