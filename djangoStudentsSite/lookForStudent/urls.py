from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.look_student_main, name='look_student_main'),
    path('blank/<slug:student_slug>/', views.student_blank, name='student_blank'),
    path('category/<slug:category_slug>', views.specialization_category, name = 'specialization_category')
]