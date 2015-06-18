from django.shortcuts import render, redirect
from account.forms import RegisterForm

def register_page(request):
	if request.POST:
		form = RegisterForm(data=request.POST)
		if form.is_valid():
			user = form.save()
			return redirect('/')
		return render(request, 'register.html', {'form': form})
	return render(request, 'register.html', {'form': RegisterForm()})
