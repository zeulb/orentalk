from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.utils.translation import gettext as _

class RegisterForm(UserCreationForm):

	password1 = forms.CharField(label=_("Password"),
		widget=forms.PasswordInput(attrs={
				'class': 'form-control',
			}))

	password2 = forms.CharField(label=_("Password confirmation"),
		widget=forms.PasswordInput(attrs={
				'class': 'form-control',
			}))
	
	class Meta(UserCreationForm.Meta):
		widgets = {
			'username': forms.fields.TextInput(attrs={
				'class': 'form-control',
			}),
		}

class LoginForm(AuthenticationForm):

	username = forms.CharField(max_length=254, 
		widget=forms.TextInput(attrs={
				'class': 'form-control',
			}))
	password = forms.CharField(label=_("Password"), 
    	widget=forms.PasswordInput(attrs={
				'class': 'form-control',
			}))