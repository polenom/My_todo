from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class UserToDo(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, db_column="user")
    timeCreate = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=30)
    text = models.TextField(null=True, blank=True, default='')
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Register(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=30)