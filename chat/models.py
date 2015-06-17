from django.db import models

class Room(models.Model):

	title = models.TextField(default='')
