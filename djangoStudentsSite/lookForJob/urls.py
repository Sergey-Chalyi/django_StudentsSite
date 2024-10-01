from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.look_job_main, name='look_job_main')
]