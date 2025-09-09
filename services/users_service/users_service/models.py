from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)

    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username