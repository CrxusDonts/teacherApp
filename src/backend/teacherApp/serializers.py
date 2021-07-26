from rest_framework import serializers
from .models import *


class BackendAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = BackendAccount
        fields = '__all__'


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = '__all__'


class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = '__all__'
