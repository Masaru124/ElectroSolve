from django.shortcuts import render,redirect
from .models import Room
from django.contrib.auth.decorators import login_required
from .forms import RoomForm
# Create your views here.
def room(request,pk):
    rooms=Room.objects.all()
    context={'rooms':rooms}
    return render(request,'room.html',context)

@login_required
def room_form(request):
    form=RoomForm()
    if request.method=='POST':
        form=RoomForm(request.POST)
        if form.is_valid():
            room = form.save(commit=False)
            room.author = request.user
            room.save()
            return redirect('discuss')
        else:
            print(form.errors)  # Debugging line

        
    context={'form':form}
    return render(request,'room_form.html',context)