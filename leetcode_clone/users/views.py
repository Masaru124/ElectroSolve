from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views import View
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import Signup, LoginForm  
from discussionform.models import Room



class SignupView(CreateView):
    form_class = Signup  
    template_name = 'register.html'
    success_url = reverse_lazy('login')

    def form_valid(self,form):
            response=super().form_valid(form)
            username=form.cleaned_data['username']
        
            messages.success(self.request,f'account created for {username}!')
            return response


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
                print(f"User authenticated: {username}")  # Debug statement
            return redirect('homepage')
        print("Invalid credentials")  # Debug statement
        return render(request, 'login.html', {'form': form, 'error': 'Invalid credentials'})
    
@login_required
def profile(request):
    return render(request, 'profile.html')  

@login_required
def user_logout(request):
    logout(request)  
    return redirect('homepage')

def contests(request):
    return render(request,'contests.html')

def discuss(request):
    rooms=Room.objects.all()
    context={'rooms':rooms}
    return render(request,'discuss.html',context)

def editprofile(request):
    return render(request,'editprofile.html')
