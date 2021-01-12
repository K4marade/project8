from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from .models import UserAuth
from django.forms.widgets import PasswordInput, TextInput


class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UserAuth
        fields = ['username', 'email']