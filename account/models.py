from django.contrib.auth.models import AbstractUser
from django.db import models


class UserAuth(AbstractUser):
    """
    Class that inherit from django AbstractUser to store users in database
    """

    pass
