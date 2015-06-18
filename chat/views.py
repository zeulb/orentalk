from django.shortcuts import render, redirect
from chat.forms import NewRoomForm, NewMessageForm
from chat.models import Room, Message

def home_page(request):
	if request.POST:
		form = NewRoomForm(data=request.POST)
		if form.is_valid():
			_room = form.save()
			return redirect(_room)
		return render(request, 'home.html', {'form': form, })
	else:
		return render(request, 'home.html', {'form': NewRoomForm(), })

def room_page(request, room_id):
	room = Room.objects.get(id=room_id)
	if request.POST:
		form = NewMessageForm(data=request.POST)
		if form.is_valid():
			message = form.save(room)
			return redirect(room)
		return render(request, 'room.html', {'room': room, 'form': form})
	return render(request, 'room.html', {'room': room, 'form': NewMessageForm()})