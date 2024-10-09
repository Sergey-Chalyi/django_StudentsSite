from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy

from student.forms import LoginStudentForm, RegisterStudentForm


class LoginStudent(LoginView):
    # форма класса, указываем тот, что нужно по умолчанию
    # если пользователь ввел правильные данные, то этот класс автоматом
    # перенаправляет не на ту страницу, что нам нужно -> нужно переопределить метод get_success_url
    # ИЛИ указать глобальные константы в настройках
    form_class = AuthenticationForm

    # можно указать свою форму класс, но тогда нужно, чтобы наш класс наследовался от AuthenticationForm
    # form_class = LoginStudentForm
    # имя шаблона
    template_name = 'student/login.html'
    # доп данные, передаваемые шаблону
    extra_context = {'page_title' : 'log in'}



# Create your views here.
def login_student(request: HttpRequest):
    # если мы заполнили форму и нажали на кнопку "авторизоваться
    if request.method == 'POST':
        form = LoginStudentForm(request.POST) # создаем объект формы
        if form.is_valid(): # если все поля формы заполнены корректно
            cd = form.cleaned_data # получаем словарь введенных данных
            # проверка наличия юзера в бд (в таблице, созданной джанго автоматом)
            # если есть - создается объект (в противном случае None)
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user and user.is_active: # проверка наличия юзера в бд
                login(request, user) # авторизация юзера в системе, благодаря этой функции джанго запоминает данные юзера благодаря сессиям (не нужно второй раз вводить пароль и логин)
                return HttpResponseRedirect(reverse('start_main')) # перенаправляем на главную страницу
    else: # если только в первый раз открыли страничку с формой авторизоваться
        form = LoginStudentForm() # создаем объект формы

    return render(request,'student/login.html', {'form' : form})


def logout_student(request: HttpRequest):
    logout(request) # джанго делает так, чтобы юзер вышел из сайта
    return HttpResponseRedirect('/users/student_login') # перенаправляем на страницу входа (reverse используется, когда у нас не конкретный пусть, а используется пространство именя)

def register(request: HttpRequest):
    if request.method == 'POST':
        form = RegisterStudentForm(request.POST)
        if form.is_valid():
            # формируем объект user, но не заносим в бд записи
            user = form.save(commit=False)
            # шифрование пароля и занесение его в атрибут password
            user.set_password(form.cleaned_data['password'])
            # занесение в бд
            user.save()
            return render(request, 'student/succeed_register.html')
    else:
        form = RegisterStudentForm()
    return render(request, 'student/register.html', {'form':form})


