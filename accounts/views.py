# accounts/views.py

from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import LoginRecord  # Import the model you just created


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
