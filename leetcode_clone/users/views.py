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
                messages.success(request, f'Welcome back, {username}!')
                return redirect('homepage')
            else:
                messages.error(request, 'Invalid username or password')
                return render(request, 'login.html', {'form': form})
        messages.error(request, 'Please correct the errors below')
        return render(request, 'login.html', {'form': form})
    
@login_required
def profile(request):
    user = request.user
    profile = user.profile
    context = {
        'user': user,
        'profile': profile,
        'problems_solved': profile.problems_solved,
        'streak': profile.streak,
        'max_streak': profile.max_streak,
        'rating': profile.rating,
        'easy_solved': profile.easy_solved,
        'medium_solved': profile.medium_solved,
        'hard_solved': profile.hard_solved,
    }
    return render(request, 'profile.html', context)


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

from django.contrib import messages
from .forms import ProfileEditForm

@login_required
def editprofile(request):
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, request.FILES)
        if form.is_valid():
            user = request.user
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.email = form.cleaned_data['email']
            user.profile.bio = form.cleaned_data['bio']
            user.profile.location = form.cleaned_data['location']
            user.profile.website = form.cleaned_data['website']
            if form.cleaned_data['profile_picture']:
                user.profile.profile_picture = form.cleaned_data['profile_picture']
            user.save()
            user.profile.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('profile')
    else:
        initial_data = {
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'email': request.user.email,
            'bio': request.user.profile.bio,
            'location': request.user.profile.location,
            'website': request.user.profile.website,
            'profile_picture': request.user.profile.profile_picture
        }
        form = ProfileEditForm(initial=initial_data)
    
    return render(request, 'editprofile.html', {'form': form})
