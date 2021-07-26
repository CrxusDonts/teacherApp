from django.contrib.auth.models import User
from django.db import models


class BackendAccount(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, null=True)
    open_id = models.CharField(default="", max_length=50)


class Class(models.Model):
    class_name = models.CharField(max_length=10, default="undefined")


class Manager(models.Model):
    # True 是owner False不是
    status = models.BooleanField(default=False)
    class_name = models.ForeignKey(Class, on_delete=models.CASCADE, default="undefined")
    account = models.ForeignKey(BackendAccount, on_delete=models.CASCADE)


class FrontAccount(models.Model):
    open_id = models.CharField(default="", max_length=50)


class People(models.Model):
    name = models.CharField(default="", max_length=50)
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
    front_account = models.ForeignKey(FrontAccount, on_delete=models.CASCADE, default=None)
    my_class = models.ForeignKey(Class, on_delete=models.CASCADE, default=None)


class ChoiceQuestion(models.Model):
    text_content = models.TextField(default="null")


class Options(models.Model):
    question = models.ForeignKey(ChoiceQuestion, on_delete=models.CASCADE)
    order = models.IntegerField(default=0)
    if_correct = models.BooleanField(default=False)


class Media(models.Model):
    file = models.FileField(upload_to='./media/%Y/%m/%d/')
    type_file = (
        (0, 'image'),
        (1, 'video'),
    )
    file_type = models.IntegerField(choices=type_file, default=1)
