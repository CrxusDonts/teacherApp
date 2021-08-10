from django.contrib.auth.models import User
from django.db import models, IntegrityError
from rest_framework import permissions


class BackendAccount(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, null=True)
    open_id = models.CharField(default='', max_length=50)


class Class(models.Model):
    class_name = models.CharField(max_length=20, default='undefined')


class People(models.Model):
    name = models.CharField(default='', max_length=50)
    is_teacher = models.BooleanField(default=False)
    account = models.ForeignKey(BackendAccount, related_name='account_people', on_delete=models.CASCADE, null=True)
    clazz = models.ForeignKey(Class, related_name='class_people', on_delete=models.CASCADE, null=True)


class Manager(models.Model):
    is_owner = models.BooleanField(default=False)
    clazz = models.ForeignKey(Class, related_name='class_manager', on_delete=models.CASCADE)
    account = models.ForeignKey(BackendAccount, related_name='account_manager', on_delete=models.CASCADE)


class Homework(models.Model):
    title = models.CharField(max_length=20, default='undefined')
    start_time = models.DateTimeField()
    due_time = models.DateTimeField()
    repeatable = models.BooleanField(default=False)
    clazz = models.ForeignKey(Class, on_delete=models.CASCADE)


class ChoiceQuestion(models.Model):
    text_content = models.TextField(default='null')
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE)
    is_contain_media = models.BooleanField(default=False)


class Options(models.Model):
    question = models.ForeignKey(ChoiceQuestion, related_name='ChoiceQuestion_option', on_delete=models.CASCADE)
    text_content = models.TextField(default='null')
    order = models.IntegerField(default=0)
    is_correct = models.BooleanField(default=False)


class ChoiceQuestionUserAnswer(models.Model):
    question = models.ForeignKey(ChoiceQuestion, related_name='ChoiceQuestion_answer', on_delete=models.CASCADE)
    answer_order = models.IntegerField(default=0)
    student = models.ForeignKey(People, related_name='ChoiceQuestionUser_answer', on_delete=models.CASCADE)
    is_correct = models.BooleanField(default=False)


class CompletionQuestion(models.Model):
    text_content = models.TextField(default='null')
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE, null=False)
    is_contain_media = models.BooleanField(default=False)


class CompletionQuestionAnswer(models.Model):
    answer = models.CharField(max_length=50, default='undefined')
    answer_order = models.IntegerField(default=0)
    question = models.ForeignKey(CompletionQuestion, related_name='CompletionQuestion_answer', on_delete=models.CASCADE)


class CompletionQuestionUserAnswer(models.Model):
    answer = models.CharField(max_length=50, default='undefined')
    answer_order = models.IntegerField(default=0)
    question = models.ForeignKey(CompletionQuestion, related_name='CompletionQuestionUser_answer',
                                 on_delete=models.CASCADE)
    student = models.ForeignKey(People, related_name='CompletionUser_answer', on_delete=models.CASCADE)


class SubjectiveQuestion(models.Model):
    text_content = models.TextField(default='null')
    homework = models.ForeignKey(Homework, related_name='homework_subjective', on_delete=models.CASCADE, null=False)
    is_contain_media = models.BooleanField(default=False)


class SubjectiveQuestionUserAnswer(models.Model):
    question = models.ForeignKey(SubjectiveQuestion, related_name='SubjectiveQuestion_answer', on_delete=models.CASCADE)
    student = models.ForeignKey(People, related_name='SubjectiveUser_answer', on_delete=models.CASCADE, null=True)


class JoinClassRequest(models.Model):
    class_id = models.ForeignKey(Class, related_name='class_JoinClassRequest', on_delete=models.CASCADE, null=True)
    student = models.ForeignKey(People, related_name='student_JoinClassRequest', on_delete=models.CASCADE, null=True)


class ManageInvitation(models.Model):
    inviter = models.ForeignKey(BackendAccount, related_name='account_inviter', on_delete=models.CASCADE)
    invitee = models.ForeignKey(BackendAccount, related_name='account_invitee', on_delete=models.CASCADE)
    clazz = models.ForeignKey(Class, related_name='class_invitation', on_delete=models.CASCADE)


class Media(models.Model):
    url = models.FileField(upload_to='./static/media/%Y/%m/%d/')
    type_file = (
        (0, 'image'),
        (1, 'video')
    )
    file_type = models.IntegerField(choices=type_file, default=0)
    choice_question = models.ForeignKey(ChoiceQuestion, related_name='choice_media', on_delete=models.CASCADE,
                                        null=True)
    completion_question = models.ForeignKey(CompletionQuestion, related_name='completion_media',
                                            on_delete=models.CASCADE,
                                            null=True)
    subjective_question = models.ForeignKey(SubjectiveQuestion, related_name='subjective_media',
                                            on_delete=models.CASCADE,
                                            null=True)
    subjective_question_user_answer = models.ForeignKey(SubjectiveQuestionUserAnswer,
                                                        related_name='subjective_user_answer_media',
                                                        on_delete=models.CASCADE,
                                                        null=True)


class TeacherComment(models.Model):
    text_content = models.TextField(default='null')
    pos_x = models.DecimalField(max_digits=19, decimal_places=10, default=0)
    pos_y = models.DecimalField(max_digits=19, decimal_places=10, default=0)
    time_slot = models.DecimalField(max_digits=10, decimal_places=5, default=0)
    media = models.ForeignKey(Media, related_name='Media_comment',
                              on_delete=models.CASCADE, null=True)
    url = models.FileField(upload_to='./static/media/%Y/%m/%d/')
