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


class FrontAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = FrontAccount
        fields = '__all__'


class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = People
        fields = '__all__'


class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = '__all__'


class ChoiceQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChoiceQuestion
        fields = '__all__'


class ChoiceQuestionUserAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChoiceQuestionUserAnswer
        fields = '__all__'


class OptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Options
        fields = '__all__'


class HomeworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Homework
        fields = '__all__'


class CompletionQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompletionQuestion
        fields = '__all__'
