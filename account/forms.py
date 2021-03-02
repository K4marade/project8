from django.contrib.auth.forms import UserCreationForm
from .models import UserAuth


class RegisterForm(UserCreationForm):
    """Class that defines new user register form"""

    class Meta(UserCreationForm.Meta):
        model = UserAuth
        fields = ['username', 'email']


# class LoginFormView(SuccessMessageMixin, LoginView):
#     template_name = 'registration/login.html'
#     success_url = ''
#     success_message = "You were successfully logged in"
