from django.test import TestCase
from chat.models import Room, Message
from chat.views import room_page
from chat.forms import NewMessageForm
from django.http import HttpRequest

class HomePageTest(TestCase):

	def test_can_create_new_room(self):
		self.client.post(
			'/',
			data={'title': 'Budi anduk'}
		)

		self.assertEqual(Room.objects.count(), 1)
		new_room = Room.objects.first()
		self.assertEqual(new_room.title, 'Budi anduk')

	def test_room_model_have_unique_keys(self):
		self.client.post(
			'/',
			data={'title': 'Budi anduk'}
		)

		self.client.post(
			'/',
			data={'title': 'Budi anduk'}
		)

		room = Room.objects.all()
		self.assertEqual(len(room), 2)
		self.assertNotEqual(room[0], room[1])

	def test_cannot_create_room_with_empty_title(self):
		self.client.post(
			'/',
			data={'title': ''}
		)

		self.assertEqual(Room.objects.count(), 0)


	def test_room_page_return_correct_content(self):
		self.client.post(
			'/',
			data={'title': 'Budi anduk'}
		)

		request = HttpRequest()
		html = room_page(request, 1)
		self.assertContains(html, 'Budi anduk')

	def test_can_add_message_to_a_room(self):
		self.client.post(
			'/',
			data={'title': 'Budi anduk'}
		)

		request = HttpRequest()
		html = room_page(request, 1)
		request.POST = {
			'text': 'Elooo'
		}

		room_page(request, 1)

		self.assertEqual(Message.objects.count(), 1)
		self.assertEqual(Message.objects.get(id=1).text, 'Elooo')
