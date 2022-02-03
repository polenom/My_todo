from django.db import models
from django.utils import timezone

class UserToDo(models.Model):
    username = models.CharField(max_length=20)
    timeCreate = models.DateTimeField(default=timezone.now)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.nameTask

