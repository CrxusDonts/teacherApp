from django.contrib.auth.models import User
from django.db import models, IntegrityError


class BackendAccount(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, null=True)
    open_id = models.CharField(default='', max_length=50)


class Class(models.Model):
    class_name = models.CharField(max_length=20, default="null")


class Manager(models.Model):
    status_choice = (
        (0, 'owner'),
        (1, 'manager'),
    )
    status = models.IntegerField(choices=status_choice, default=0)
    class_name = models.ForeignKey(Class, on_delete=models.CASCADE, default="undefined")
    account = models.ForeignKey(BackendAccount, on_delete=models.CASCADE)


class FrontAccount(models.Model):
    open_id = models.CharField(default='', max_length=50)


class People(models.Model):
    name = models.CharField(default='', max_length=50)
    sex_choice = (
        (0, 'female'),
        (1, 'male'),
    )
    sex = models.IntegerField(choices=sex_choice, default=1)
    type_choice = (
        (0, 'teacher'),
        (1, 'student'),
    )
    type = models.IntegerField(choices=type_choice, default=1)
    front_account = models.ForeignKey(FrontAccount, on_delete=models.CASCADE)
    my_class = models.ForeignKey(Class, on_delete=models.CASCADE)


class Homework(models.Model):
    start_time = models.DateTimeField()
    due_time = models.DateTimeField()
    repeatable = models.BooleanField(default=False)
    the_clazz = models.ForeignKey(Class, on_delete=models.CASCADE)

class ChoiceQuestion(models.Model):
    text_content = models.TextField(default="null")


class Options(models.Model):
    question = models.ForeignKey(ChoiceQuestion, on_delete=models.CASCADE)
    order = models.IntegerField(default=0)
    if_correct = models.BooleanField(default=False)


class ChoiceQuestionUserAnswer(models.Model):
    question = models.ForeignKey(ChoiceQuestion, on_delete=models.CASCADE)
    answer_order = models.IntegerField(default=0)
    user = models.ForeignKey(People, on_delete=models.CASCADE)


class Media(models.Model):
    file = models.FileField(upload_to='./media/%Y/%m/%d/')
    type_file = (
        (0, 'image'),
        (1, 'video'),
    )
    file_type = models.IntegerField(choices=type_file, default=1)


class CompletionQuestion(models.Model):
    text_content = models.TextField(default="null")
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE, null=False)
