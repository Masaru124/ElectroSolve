from django.urls import path
from . import views
from .views import register, login, profile  # Ensure all views are imported

urlpatterns = [
    path('register/', register, name='register'),  # User registration
    path('login/', login, name='login'),            # User login
    path('profile/', profile, name='profile'),      # User profile

]
