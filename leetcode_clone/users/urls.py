from django.urls import path
from .views import SignupView, login, profile, user_logout  # Ensure all views are imported

urlpatterns = [
    path('register/', SignupView.as_view(), name='Signup'),  # User registration
    path('login/', login, name='login'),            # User login
    path('profile/', profile, name='profile'),      # User profile
    path('logout/', user_logout, name='logout'),    # User logout
]
