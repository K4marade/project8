# from django.contrib.auth.models import User, AbstractUser
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from account.models import UserAuth


class RegisterForm(ModelForm):
    class Meta:
        model = UserAuth
        fields = ['username', 'email', 'password']


# class RegisterForm(ModelForm):
#     pass

#
# class UserForm(ModelForm):
#     class Meta:
#         fields = ['username', ]
