from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.startPage),
    path('test', views.test),
    path('register/', views.registerUser),
    path('todo/delete', views.deletetodo, name='deletetodo'),
    path('todo/logout', views.logoutuser, name='logoutuser'),
    path('todo', views.pageToDo),
    path('todo/<int:pk>',views.pageoneToDo, name='onetodo' ),
    path('register/checkuser', views.checkUserName)
]