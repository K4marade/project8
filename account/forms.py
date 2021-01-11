# from django.contrib.auth.models import User, AbstractUser
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm
from account.models import UserAuth


class RegisterForm(ModelForm):
    class Meta:
        model = UserAuth
        fields = ['username', 'email', 'password', 'password2']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'input100',
                                               'name': 'name',
                                               'placeholder': 'username'}),

            'email': forms.EmailInput(attrs={'class': 'input100',
                                             'name': 'email',
                                             'placeholder': '@'}),

            'password': forms.PasswordInput(attrs={'class': 'input100',
                                                   'name': 'pass',
                                                   'placeholder': '****'}),

            'password2': forms.PasswordInput(attrs={'class': 'input100',
                                                    'name': 'repeat-pass',
                                                    'placeholder': '****'})

        }
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
