from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.startPage),
    path('test', views.test)
]