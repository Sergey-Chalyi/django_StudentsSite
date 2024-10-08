from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm


class LoginStudentForm(forms.Form):
    username = forms.CharField(max_length=255, label='loginnnn', widget=forms.TextInput())
    password = forms.CharField(max_length=255, label='passwordddd', widget=forms.PasswordInput())
    class Meta:
        # указываем, с какой таблицей в бд мы связываем данную форму
        # по умолчанию джанго сам выбирает свою созданную с начала
        model = get_user_model()
        fields = ['username', 'password']

