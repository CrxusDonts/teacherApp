from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from .serializers import *


# Create your views here.
class BackendAccountView(viewsets.ModelViewSet):
    queryset = BackendAccount.objects.all()
    serializer_class = BackendAccountSerializer

    # 注册后台账户
    @action(methods=['post'], detail=False)
    def register(self, request):
        user_name = request.data.get('user_name')
        password = request.data.get('password')
        try:
            new_user = User.objects.create_user(username=user_name, password=password)
        except:
            return Response('The user already exited')
        new_backend_account = BackendAccount.objects.create(user=new_user)
        new_backend_account.save()
        serializer = self.get_serializer(new_backend_account)
        return Response(serializer.data)

    # 更改账户的密码
    @action(methods=['put'], detail=False)
    def change_password(self, request):
        user_name = request.data.get('user_name')
        password = request.data.get('password')
        try:
            user = User.objects.get(username=user_name)
        except:
            return Response('The user is not exited')
        user.set_password(password)
        user.save()
        serializer = self.get_serializer(user)
        return HttpResponse(status=200)


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
