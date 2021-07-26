from rest_framework import serializers
from .models import BackendAccount


class BackendAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = BackendAccount
        fields = '__all__'
