# tasks/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.helloworld),
    path('Helloworld/', views.helloworld),
]