import uuid
from datetime import datetime
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


class User(AbstractUser):
    """
    DESCRIPTION
    """
    email = models.EmailField(verbose_name='email', max_length=60, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

