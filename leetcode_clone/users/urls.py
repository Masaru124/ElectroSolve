from django.urls import path,include
from .views import SignupView, profile, user_logout, LoginView ,contests,discuss,editprofile

urlpatterns = [
    path('register/', SignupView.as_view(), name='Signup'),  
    path('login/', LoginView.as_view(), name='login'),            # User login
    path('profile/', profile, name='profile'),      
    path('logout/', user_logout, name='logout'), 
    path('contests/' , contests,name='contests'),
    path('discuss/',discuss,name='discuss'),
    path('editprofile/',editprofile,name='editprofile'),
    path('',include('discussionform.urls'))

]
