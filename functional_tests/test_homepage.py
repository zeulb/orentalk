from .base import FunctionalTest

class TestHomePage(FunctionalTest):

	def test_redirected_when_creating_new_chat_room(self):
		self.browser.get(self.live_server_url)

		current_url = self.browser.current_url
		
		new_chat_form = self.browser.find_element_by_id('new-chat')
		new_chat_form.send_keys('Gajah terbang\n')

		new_url = self.browser.current_url

		self.assertNotEqual(current_url, new_url)