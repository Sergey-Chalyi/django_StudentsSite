from django.urls import path
from django.contrib.auth.views import LogoutView

from student import views

app_name = 'users'

urlpatterns = [
    path('login/', views.LoginStudent.as_view(), name='student_login'),
    path('logout/', LogoutView.as_view(), name='student_logout')
]
