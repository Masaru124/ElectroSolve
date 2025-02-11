from django.urls import path
from .views import SignupView, profile, user_logout, LoginView  # Ensure all views are imported

urlpatterns = [
    path('register/', SignupView.as_view(), name='Signup'),  
    path('login/', LoginView.as_view(), name='login'),            # User login
    path('profile/', profile, name='profile'),      
    path('logout/', user_logout, name='logout'),    
]
