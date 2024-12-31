from django.contrib.auth.models import AbstractUser
from django.db import models

SEX_CHOICES = {("male", "Male"), ("female", "Female")}


class User(AbstractUser):
    birth_date = models.DateField(null=True, blank=True)
    sex = models.CharField(choices=SEX_CHOICES, null=True, blank=True)
    bio = models.TextField()
    is_host = models.BooleanField(default=False)
