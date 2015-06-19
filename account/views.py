from django.shortcuts import render, redirect
from account.forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def register_page(request):
	is_guest = False
	if request.user.is_authenticated():
		is_guest = hasattr(request.user, 'additional') and request.user.additional.is_guest
		if not is_guest:
			return redirect('/')

	if request.POST:
		form = RegisterForm(data=request.POST)
		if form.is_valid():
			user = form.save()
			messages.success(request, 'Successfully registered, you can now login')
			return redirect('/')
		return render(request, 'register.html', {'form': form})
	return render(request, 'register.html', {'form': RegisterForm()})

def login_page(request):
	is_guest = False
	if request.user.is_authenticated():
		is_guest = hasattr(request.user, 'additional') and request.user.additional.is_guest
		if not is_guest:
			return redirect('/')

	if request.POST:
		form = LoginForm(data=request.POST)
		user = authenticate(username=request.POST['username'], password=request.POST['password'])
		if form.is_valid() and user:
			if is_guest:
				logout(request)
			login(request, user)
			messages.success(request, 'Welcome %s !' % (user.username, ))
			return redirect('/')
		return render(request, 'login.html', {'form': form})
	return render(request, 'login.html', {'form': LoginForm()})

def logout_page(request):
	logout(request)
	return redirect('/')