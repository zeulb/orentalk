from django.shortcuts import render, redirect
from account.forms import RegisterForm

def register_page(request):
	if request.user:
		return redirect('home')
	return render(request, 'register.html', {'form': RegisterForm})