from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings

class Room(models.Model):

	title = models.TextField(default='')
	owner = models.ForeignKey(settings.AUTH_USER_MODEL, default=None)

	def get_absolute_url(self):
		return reverse('room', args=[self.id])

class Message(models.Model):

	text = models.TextField(default='')
	room = models.ForeignKey(Room, default=None)
	owner = models.ForeignKey(settings.AUTH_USER_MODEL, default=None)

