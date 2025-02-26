# AirQualityMonitor/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # This line includes all the URLs defined in accounts/urls.py
    path('accounts/', include('accounts.urls')),
]
