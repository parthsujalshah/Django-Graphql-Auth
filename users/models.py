from django.db import models
from django.contrib.auth.models import AbstractUser


class ExtendedUser(AbstractUser):
    email = models.EmailField(blank=False, max_length=255)

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'   