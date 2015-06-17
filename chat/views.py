from django.shortcuts import render, redirect
from chat.forms import NewRoomForm

def home_page(request):
	if request.POST:
		room = NewRoomForm(data=request.POST)
		if room.is_valid():
			room.save()
			return redirect('/')
		return render(request, 'home.html', {'form': room, })
	else:
		return render(request, 'home.html', {'form': NewRoomForm(), })

def room(request):
	pass