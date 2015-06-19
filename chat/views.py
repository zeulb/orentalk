from django.shortcuts import render, redirect
from chat.forms import NewRoomForm, NewMessageForm
from chat.models import Room, Message
from account.models import Additional
from django.contrib.auth import get_user_model
User = get_user_model()

def home_page(request):
	if request.POST:
		form = NewRoomForm(data=request.POST)
		if form.is_valid():
			if request.user.is_authenticated():
				_room = form.save(request.user)
			else:
				user = Additional.create_guest()
				_room = form.save(user)
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
