from django.urls import path
from .views import room

urlpatterns = [
    path('room/<str:pk>',room,name='Room'),

]
