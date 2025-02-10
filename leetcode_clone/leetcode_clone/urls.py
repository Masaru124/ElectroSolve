from django.contrib import admin
from django.urls import path, include
from problems.views import homepage  # Import the homepage view

from users.views import SignupView  # Import the Signup view

urlpatterns = [
    path('register/', SignupView.as_view(), name='register'),  # Add this line for the registration
    path('', homepage, name='homepage'),  # Add this line for the homepage
    path('admin/', admin.site.urls),
    path('problems/', include('problems.urls')),  # Include problems app URLs
    path('users/', include('users.urls')),  # Include users app URLs
]
