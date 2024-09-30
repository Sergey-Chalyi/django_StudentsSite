from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.support_main, name='support_main')
]
