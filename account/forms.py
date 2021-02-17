from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.forms import ModelForm
from django import forms
from .models import UserAuth
from django.forms.widgets import PasswordInput, TextInput


class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UserAuth
        fields = ['username', 'email']


# class LoginFormView(SuccessMessageMixin, LoginView):
#     template_name = 'registration/login.html'
#     success_url = ''
#     success_message = "You were successfully logged in"
