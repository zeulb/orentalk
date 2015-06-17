from django.test import TestCase
from chat.models import Room

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
