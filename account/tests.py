from django.test import TestCase
from django.http import HttpRequest
from account.views import register_page
from django.contrib.auth import get_user_model
User = get_user_model()

class RegisterTest(TestCase):

	def test_can_register(self):
		request = HttpRequest()
		request.POST = {
			'username': 'budianduk',
			'password1': 'anduk4ever',
			'password2': 'anduk4ever'
		}

		register_page(request)

		self.assertEqual(User.objects.count(), 1)

		self.assertEqual(User.objects.first().username, 'budianduk')


	def test_cannot_register_username_that_already_exist(self):
		request = HttpRequest()
		request.POST = {
			'username': 'budianduk',
			'password1': 'anduk4ever',
			'password2': 'anduk4ever'
		}

		register_page(request)
		register_page(request)

		self.assertEqual(User.objects.count(), 1)