from django.contrib.auth.models import AbstractUser
from django.db import models


class UserAuth(AbstractUser):
    password2 = models.CharField(max_length=50, default=None)

