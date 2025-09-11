from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

class User(AbstractUser):
    is_supervisor = models.BooleanField(default=False)
    token_invalid_before = models.DateTimeField(default=timezone.now)
    role = models.CharField(max_length=20, default="user")
