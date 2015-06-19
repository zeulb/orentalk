from django import forms
from chat.models import Room, Message


EMPTY_TITLE_ERROR = "You can't create a room with blank title"
EMPTY_MESSAGE_ERROR = "You need to type something"

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

	def save(self, owner):
		return Room.objects.create(title=self.cleaned_data['title'], owner=owner)

class NewMessageForm(forms.models.ModelForm):

	class Meta:
		model = Message
		fields = ('text',)
		widgets = {
			'text': forms.fields.TextInput(attrs={
				'placeholder': 'Type something here!',
				'class': 'form-control',
			}),
		}
		error_messages = {
			'text': {'required': EMPTY_MESSAGE_ERROR}
		}

	def save(self, room, owner):
		return Message.objects.create(text=self.cleaned_data['text'], room=room, owner=owner)
