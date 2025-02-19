# accounts/views.py

from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import LoginRecord
from django.contrib.auth.models import User


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Log the user in
            user = form.get_user()
            login(request, user)

            # Create a new login record
            ip_address = request.META.get('REMOTE_ADDR')  # Capture the client IP address
            record = LoginRecord(user=user, ip_address=ip_address)
            record.save()

            # Redirect after login (change 'home' to your desired URL name)
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})


def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        # Add any additional validations here
        try:
            User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, "Account created successfully!")
            return redirect('login')  # Redirect to login or another page
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")
    return render(request, 'accounts/login.html')

def data_view(request):
    if request.method == 'GET':
        return render(request, 'accounts/dataPage.html')

def trends_view(request):
    if request.method == 'GET':
        return render(request, 'accounts/trendsPage.html')
