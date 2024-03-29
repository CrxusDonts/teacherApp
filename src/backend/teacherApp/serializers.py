from rest_framework import serializers
from .models import BackendAccount, Class, Manager, People, Options, ChoiceQuestion, ChoiceQuestionUserAnswer, Media, \
    Homework, CompletionQuestion, CompletionQuestionAnswer, SubjectiveQuestion, CompletionQuestionUserAnswer, \
    SubjectiveQuestionUserAnswer, TeacherComment, JoinClassRequest, ManageInvitation


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


class CompletionQuestionAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompletionQuestionAnswer
        fields = '__all__'


class CompletionQuestionUserAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompletionQuestionUserAnswer
        fields = '__all__'


class SubjectiveQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubjectiveQuestion
        fields = '__all__'


class SubjectiveQuestionUserAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubjectiveQuestionUserAnswer
        fields = '__all__'


class TeacherCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherComment
        fields = '__all__'


class JoinClassRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = JoinClassRequest
        fields = '__all__'


class ManageInvitationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManageInvitation
        fields = '__all__'
