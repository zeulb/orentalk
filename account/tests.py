from django.test import TestCase
from django.http import HttpRequest
from account.views import register_page, login_page
from django.contrib.auth import get_user_model
from django.contrib.sessions.backends.db import SessionStore
from django.core.urlresolvers import reverse

User = get_user_model()

class RegisterTest(TestCase):

	def test_can_register(self):
		self.client.post(reverse('register'),data={
			'username': 'budianduk',
			'password1': 'anduk4ever',
			'password2': 'anduk4ever'
		})

		self.assertEqual(User.objects.count(), 1)

		self.assertEqual(User.objects.first().username, 'budianduk')


	def test_cannot_register_username_that_already_exist(self):
		self.client.post(reverse('register'),data={
			'username': 'budianduk',
			'password1': 'anduk4ever',
			'password2': 'anduk4ever'
		})

		self.client.post(reverse('register'),data={
			'username': 'budianduk',
			'password1': 'anduk4ever',
			'password2': 'anduk4ever'
		})


		self.assertEqual(User.objects.count(), 1)

	def test_can_login(self):
		User.objects.create_user(username='budianduk', password='anduk4ever')

		response = self.client.post(reverse('login'), {
			'username': 'budianduk',
			'password': 'anduk4ever',
		})

		self.assertRedirects(response, reverse('home'))

	def test_cannot_login_with_wrong_password(self):
		User.objects.create_user(username='budianduk', password='anduk4ever')

		response = self.client.post(reverse('login'), {
			'username': 'budianduk',
			'password': 'anduknot4ever',
		})

		self.assertTemplateUsed(response, 'login.html')

	def test_can_logout(self):
		User.objects.create_user(username='budianduk', password='anduk4ever')

		self.client.post(reverse('login'), {
			'username': 'budianduk',
			'password': 'anduk4ever',
		})

		self.assertIn('_auth_user_id', self.client.session)

		self.client.get(reverse('logout'))

		self.assertNotIn('_auth_user_id', self.client.session)

	def test_guest_can_register(self):
		self.client.post(
			'/',
			data={'title': 'Budi anduk'}
		)

		self.assertEqual(User.objects.count(), 1)
		
		self.client.post(reverse('register'),data={
			'username': 'budianduk',
			'password1': 'anduk4ever',
			'password2': 'anduk4ever'
		})


		self.assertEqual(User.objects.count(), 2)

		self.assertEqual(User.objects.all()[1].username, 'budianduk')

	def test_guest_can_login(self):
		self.client.post(
			'/',
			data={'title': 'Budi anduk'}
		)
		self.test_can_login()

	def test_guest_can_register_and_logout(self):
		self.client.post(
			'/',
			data={'title': 'Budi anduk'}
		)
		self.test_can_logout()

	def test_guest_can_logout(self):
		self.client.post(
			'/',
			data={'title': 'Budi anduk'}
		)

		self.assertIn('_auth_user_id', self.client.session)

		self.client.get(reverse('logout'))

		self.assertNotIn('_auth_user_id', self.client.session)

	def test_member_cannot_login_or_register(self):

		User.objects.create_user(username='budianduk', password='anduk4ever')

		self.client.post(reverse('login'), {
			'username': 'budianduk',
			'password': 'anduk4ever',
		})

		response = self.client.get(reverse('login'))
		self.assertRedirects(response, reverse('home'))

		response = self.client.get(reverse('register'))
		self.assertRedirects(response, reverse('home'))
