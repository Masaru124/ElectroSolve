from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views import View
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import Signup, LoginForm  
class SignupView(CreateView):
    form_class = Signup  
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('login')

class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form}) 

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('homepage') 
        return render(request, 'login.html', {'form': form, 'error': 'Invalid credentials'}) 
@login_required
def profile(request):
    return render(request, 'profile.html')  

@login_required
def user_logout(request):
    logout(request)  
    return redirect('homepage')  
