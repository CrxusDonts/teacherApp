from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
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

class MediaView(viewsets.ModelViewSet):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer