from django.db import models
import string
import random

from django.conf import settings
from django.contrib.auth.models import User


class Additional(models.Model):

	user = models.OneToOneField(settings.AUTH_USER_MODEL)
	is_guest = models.BooleanField(default=False)

	@staticmethod
	def create_guest():
		username = 'Guest_'+''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))
		password = settings.SECRET_KEY
		user = User.objects.create_user(username=username, password=password)
		additional = Additional.objects.create(user=user, is_guest=True)
		return user