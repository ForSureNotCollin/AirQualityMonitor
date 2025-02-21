# accounts/urls.py

from django.urls import path
from .views import login_view, signup_view, data_view, trends_view, home_view

urlpatterns = [
    # '' means that going to /accounts/ will invoke login_view
    path('', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('home/', home_view, name='home'),
    path('data/', data_view, name='data'),
    path('trends/', trends_view, name='trends'),
]
