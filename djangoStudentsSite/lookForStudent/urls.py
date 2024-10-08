from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.LookForStudentHome.as_view(), name='look_student_main'),
    path('category/<slug:category_slug>', views.specialization_category, name = 'specialization_category'),
    path('blank/<slug:student_slug>/', views.student_blank, name='student_blank'),
    path('new_blank/', views.CreateNewBlank.as_view(), name='new_student_blank')
]