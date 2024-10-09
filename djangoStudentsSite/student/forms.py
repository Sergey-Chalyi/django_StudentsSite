from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm


class LoginStudentForm(forms.Form):
    username = forms.CharField(max_length=255, label='login', widget=forms.TextInput())
    password = forms.CharField(max_length=255, label='password', widget=forms.PasswordInput())
    class Meta:
        # указываем, с какой таблицей в бд мы связываем данную форму
        # по умолчанию джанго сам выбирает свою созданную с начала
        model = get_user_model()
        fields = ['username', 'password']


class RegisterStudentForm(forms.ModelForm):
    username = forms.CharField(max_length=255, label='login', widget=forms.TextInput())
    password = forms.CharField(max_length=255, label='password', widget=forms.PasswordInput())
    password2 = forms.CharField(max_length=255, label='password2', widget=forms.PasswordInput())
    class Meta:
        # указываем, с какой таблицей в бд мы связываем данную форму
        # по умолчанию джанго сам выбирает свою созданную с начала
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name', 'password', 'password2']

    # метод для проверки правильности введения пароля
    # благодаря нему будет выводиться ошибка если что-то не так
    def clean_password(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if password and password2 and password != password2:
            raise forms.ValidationError('The passwords aren\'t the same')

        return cleaned_data.get('password')

    # метод для проверки правильности введения почты
    # благодаря нему будет выводиться ошибка если что-то не так
    def clean_email(self):
        if get_user_model().objects.all().filter(email=self.cleaned_data['email']).exists():
            raise forms.ValidationError('Such email already exists')
        return self.cleaned_data['email']
