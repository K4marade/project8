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

        widgets = {
            'username': forms.TextInput(attrs={'class': 'input100',
                                               'name': 'name',
                                               'placeholder': 'username'}),

            'email': forms.EmailInput(attrs={'class': 'input100',
                                             'name': 'email',
                                             'placeholder': '@'}),

            'password1': forms.PasswordInput(attrs={'class': 'input100',
                                                    'name': 'pass',
                                                    'placeholder': '****'}),

            'password2': forms.PasswordInput(attrs={'class': 'input100',
                                                    'name': 'repeat-pass',
                                                    'placeholder': '****'})
        }


# class LoginForm(AuthenticationForm):
#     class Meta:
#         model = User
#         fields = ['username', 'password']

#     password = forms.CharField(widget=PasswordInput(attrs={'class': 'input100',
#                                                            'placeholder': '****'}))

# class RegisterForm(ModelForm):
#     class Meta:
#         model = UserAuth
#         fields = ['username', 'email', 'password', 'password2']
#
#         widgets = {
#             'username': forms.TextInput(attrs={'class': 'input100',
#                                                'name': 'name',
#                                                'placeholder': 'username'}),
#
#             'email': forms.EmailInput(attrs={'class': 'input100',
#                                              'name': 'email',
#                                              'placeholder': '@'}),
#
#             'password': forms.PasswordInput(attrs={'class': 'input100',
#                                                    'name': 'pass',
#                                                    'placeholder': '****'}),
#
#             'password2': forms.PasswordInput(attrs={'class': 'input100',
#                                                     'name': 'repeat-pass',
#                                                     'placeholder': '****'})
#
#         }
# def __init__(self, *args, **kwargs):
#     super().__init__(*args, **kwargs)
#     self.fields[''].widget.attrs.update({'class': 'special'})
#     self.fields['comment'].widget.attrs.update(size='40')

# class RegisterForm(ModelForm):
#     pass

#
# class UserForm(ModelForm):
#     class Meta:
#         fields = ['username', ]
