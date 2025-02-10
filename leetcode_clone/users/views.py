from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate, logout
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import Signup  # Import the Signup form from forms.py

class SignupView(CreateView):
    form_class = Signup  # Ensure this references the Signup form from forms.py
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('login')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('homepage')  # Redirect to homepage after login
    return render(request, 'login.html')

def profile(request):
    return render(request, 'profile.html')  # Render the profile template

def user_logout(request):
    logout(request)  # Log the user out
    return redirect('homepage')  # Redirect to homepage after logout
