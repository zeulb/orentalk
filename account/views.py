from django.shortcuts import render, redirect
from account.forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login, logout

def register_page(request):
	if request.POST:
		form = RegisterForm(data=request.POST)
		if form.is_valid():
			user = form.save()
			return redirect('/')
		return render(request, 'register.html', {'form': form})
	return render(request, 'register.html', {'form': RegisterForm()})

def login_page(request):
	if request.POST:
		form = LoginForm(data=request.POST)
		user = authenticate(username=request.POST['username'], password=request.POST['password'])
		if form.is_valid() and user:
			login(request, user)
			return redirect('/')
		return render(request, 'login.html', {'form': form})
	return render(request, 'login.html', {'form': LoginForm()})

def logout_page(request):
	logout(request)
	return redirect('/')