from django.contrib.auth.models import AbstractUser
from django.db import models
class CustomUser(AbstractUser):
    id = models.BigAutoField(primary_key=True)
    age = models.PositiveIntegerField(null=True, blank=True)