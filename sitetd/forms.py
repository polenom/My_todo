from django.forms import ModelForm
from .models import UserToDo, Register


class createTodo(ModelForm):
    class Meta:
        model = UserToDo
        fields = ['username','timeCreate','title','text', 'status']

class ToDoForm(ModelForm):
    class Meta:
        model = Register
        fields = ['username','password']
        labels = {
            'nameTask':'Задача',
        }

class RegisterForm(ModelForm):
    class Meta:
        model = Register
        fields = ['username', 'password', 'email']
