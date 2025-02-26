from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, LoginRecord

# Register CustomUser with the built-in UserAdmin for a familiar interface.
admin.site.register(CustomUser, UserAdmin)
admin.site.register(LoginRecord)
