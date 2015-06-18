from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext as _

class RegisterForm(UserCreationForm):

	password1 = forms.CharField(label=_("Password"),
        widget=forms.PasswordInput(attrs={
				'class': 'form-control',
			}))

	password2 = forms.CharField(label=_("Password confimation"),
        widget=forms.PasswordInput(attrs={
				'class': 'form-control',
			}))
	
	class Meta(UserCreationForm.Meta):
		widgets = {
			'username': forms.fields.TextInput(attrs={
				'class': 'form-control',
			}),
		}