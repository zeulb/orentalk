from django.shortcuts import render, redirect
from chat.forms import NewRoomForm

def home_page(request):
	return render(request, 'home.html', {'form': NewRoomForm(), })

def new_room(request):
	room = NewRoomForm(data=request.POST)
	if room.is_valid():
		room.save()
		return redirect('/')
	return render(request, 'home.html', {'form': NewRoomForm(), })