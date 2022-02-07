from django.contrib import admin
from .models import UserToDo

class UserToDoAdmin(admin.ModelAdmin):
    list_display = ('title','username')

admin.site.register(UserToDo, UserToDoAdmin)
# Register your models here.
