from django.urls import path
from . import views

urlpatterns = [
    path('room/<str:pk>',views.room,name='Room'),
    path('create-room/',views.room_form,name='Room_form'),
]
