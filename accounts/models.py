from django.conf import settings
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.utils import timezone

class CustomUser(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        related_name='custom_users',  # changed from the default "user_set"
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions',  # changed from the default "user_set"
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )

    def __str__(self):
        return self.username

class LoginRecord(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    login_time = models.DateTimeField(default=timezone.now)
    ip_address = models.GenericIPAddressField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} logged in at {self.login_time}"
