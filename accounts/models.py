from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.utils import timezone


class CustomUser(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        related_name='custom_users',  # change from the default "user_set"
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )

    # Override the user_permissions field similarly.
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions',  # change from the default "user_set"
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )
class User(models.Model):
    username = models.CharField(max_length=32 , unique=True)
    password = models.CharField(max_length=32)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username
# Create your models here.

class LoginRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    login_time = models.DateTimeField(default=timezone.now)
    ip_address = models.GenericIPAddressField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} logged in at {self.login_time}"