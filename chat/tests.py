from django.test import TestCase
from chat.models import Room

class HomePageTest(TestCase):

	def test_can_create_new_room(self):
		self.client.post(
			'/talk/newroom',
			data={'title': 'Budi anduk'}
		)

		self.assertEqual(Room.objects.count(), 1)
		new_room = Room.objects.first()
		self.assertEqual(new_room.title, 'Budi anduk')

