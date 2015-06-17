from .base import FunctionalTest

class TestHomePage(FunctionalTest):

	def test_create_chat_room(self):
		self.browser.get(self.live_server_url)