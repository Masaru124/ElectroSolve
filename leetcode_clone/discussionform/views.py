from django.shortcuts import render
from .models import Room
from .forms import RoomForm
# Create your views here.
def room(request,pk):
    rooms=Room.objects.all()
    context={'rooms':rooms}
    return render(request,'room.html',context)

def room_form(request):
    form=RoomForm()
    context={'form':form}
    return render(request,'room_form.html',context)