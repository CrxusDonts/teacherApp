from django.contrib.auth.models import User
from django.db import models, IntegrityError
from rest_framework import permissions


class BackendAccount(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, null=True)
    open_id = models.CharField(default='', max_length=50)


class Class(models.Model):
    class_name = models.CharField(max_length=20, default='undefined')


class Manager(models.Model):
    is_owner = models.BooleanField(default=False)
    clazz = models.ForeignKey(Class, related_name='class_manager', on_delete=models.CASCADE)
    account = models.ForeignKey(BackendAccount, related_name='account_manager', on_delete=models.CASCADE)


class FrontAccount(models.Model):
    open_id = models.CharField(default='', max_length=50)


class People(models.Model):
    name = models.CharField(default='', max_length=50)
    is_male = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    front_account = models.ForeignKey(FrontAccount, on_delete=models.CASCADE)
    clazz = models.ForeignKey(Class, on_delete=models.CASCADE)


class Homework(models.Model):
    title = models.CharField(max_length=20, default='undefined')
    start_time = models.DateTimeField()
    due_time = models.DateTimeField()
    repeatable = models.BooleanField(default=False)
    clazz = models.ForeignKey(Class, on_delete=models.CASCADE)


class ChoiceQuestion(models.Model):
    text_content = models.TextField(default='null')
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE)


class Options(models.Model):
    question = models.ForeignKey(ChoiceQuestion, on_delete=models.CASCADE)
    order = models.IntegerField(default=0)
    if_correct = models.BooleanField(default=False)


class ChoiceQuestionUserAnswer(models.Model):
    question = models.ForeignKey(ChoiceQuestion, on_delete=models.CASCADE)
    answer_order = models.IntegerField(default=0)
    user = models.ForeignKey(People, on_delete=models.CASCADE)


class CompletionQuestion(models.Model):
    text_content = models.TextField(default='null')
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE, null=False)


class CompletionQuestionAnswer(models.Model):
    answer = models.CharField(max_length=50, default='undefined')
    answer_order = models.IntegerField(default=0)
    question = models.ForeignKey(CompletionQuestion, on_delete=models.CASCADE)


class CompletionQuestionUserAnswer(models.Model):
    answer = models.CharField(max_length=50, default='undefined')
    answer_order = models.IntegerField(default=0)
    question = models.ForeignKey(CompletionQuestion, on_delete=models.CASCADE)


class SubjectiveQuestion(models.Model):
    text_content = models.TextField(default='null')
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE, null=False)


class SubjectiveQuestionUserAnswer(models.Model):
    answer = models.CharField(max_length=50, default='undefined')
    question = models.ForeignKey(SubjectiveQuestion, on_delete=models.CASCADE)


class TeacherComment(models.Model):
    text_content = models.TextField(default='null')


class JoinClassRequest(models.Model):
    class_id = models.IntegerField(default=0)
    people = models.ForeignKey(People, on_delete=models.CASCADE)


class ManageInvitation(models.Model):
    inviter = models.ForeignKey(BackendAccount, related_name='account_inviter', on_delete=models.CASCADE)
    invitee = models.ForeignKey(BackendAccount, related_name='account_invitee', on_delete=models.CASCADE)
    clazz = models.ForeignKey(Class, related_name='class_invitation', on_delete=models.CASCADE)


class Media(models.Model):
    file = models.FileField(upload_to='./media/%Y/%m/%d/')
    type_file = (
        (0, 'image'),
        (1, 'video'),
    )
    file_type = models.IntegerField(choices=type_file, default=1)
    teacher_comment = models.ForeignKey(TeacherComment, on_delete=models.CASCADE, null=True)
    choice_question = models.ForeignKey(ChoiceQuestion, on_delete=models.CASCADE, null=True)
    completion_question = models.ForeignKey(CompletionQuestion, on_delete=models.CASCADE, null=True)
    subjective_question = models.ForeignKey(SubjectiveQuestion, on_delete=models.CASCADE, null=True)
    subjective_question_user_answer = models.ForeignKey(SubjectiveQuestionUserAnswer,
                                                        on_delete=models.CASCADE, null=True)
