from django.shortcuts import render
from .models import Room

# Create your views here.
def room(request,pk):
    rooms=Room.objects.all()
    context={'rooms':rooms}
    return render(request,'room.html',context)

