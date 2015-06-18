from django.db import models
from django.core.urlresolvers import reverse

class Room(models.Model):

	title = models.TextField(default='')

	def get_absolute_url(self):
		return reverse('room', args=[self.id])


class Message(models.Model):

	text = models.TextField(default='')
	room = models.ForeignKey(Room, default=None)
