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
