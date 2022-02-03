from django.forms import ModelForm
from .models import UserToDo


class ToDoForm(ModelForm):
    class Meta:
        model = UserToDo
        fields = ['username','password']
        labels = {
            'nameTask':'Задача',
        }