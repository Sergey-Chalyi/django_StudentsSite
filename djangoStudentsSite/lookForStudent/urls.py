from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.look_student_main, name='look_student_main')
]