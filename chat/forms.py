from django import forms
from chat.models import Room


EMPTY_TITLE_ERROR = "You can't create a room with blank title"

class NewRoomForm(forms.models.ModelForm):

	class Meta:
		model = Room
		fields = ('title',)
		widgets = {
			'title': forms.fields.TextInput(attrs={
				'placeholder': 'Enter title for your room',
				'class': 'form-control input-lg',
			}),
		}
		error_messages = {
			'title': {'required': EMPTY_TITLE_ERROR}
		}
