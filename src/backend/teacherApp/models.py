from django.contrib.auth.models import User
from django.db import models


class BackendAccount(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, null=True)
    open_id = models.CharField(default="", max_length=50)


class Class(models.Model):
    class_name = models.CharField(max_length=10, default="undefined")
