from django.shortcuts import render, redirect
from chat.forms import NewRoomForm
from chat.models import Room

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
	return render(request, 'room.html', {'title': room.title, })