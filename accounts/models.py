from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    pass

class User(models.Model):
    username = models.CharField(max_length=32 , unique=True)
    password = models.CharField(max_length=32)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username
# Create your models here.