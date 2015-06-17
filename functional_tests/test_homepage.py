from .base import FunctionalTest

class TestHomePage(FunctionalTest):

	def test_redirected_when_creating_new_chat_room(self):
		self.browser.get(self.live_server_url)

		current_url = self.browser.current_url
		
		new_chat_form = self.browser.find_element_by_id('id-title')
		new_chat_form.send_keys('Gajah terbang\n')

		new_url = self.browser.current_url

		self.assertNotEqual(current_url, new_url)

	def test_new_chat_room_contain_page_title(self):
		self.browser.get(self.live_server_url)
		
		new_chat_form = self.browser.find_element_by_id('id-title')
		new_chat_form.send_keys('Gajah terbang lagi\n')

		page-title = self.browser.find_element_by_id('id-title').text

		self.assertNotEqual(page-title, 'Gajah terbang lagi')
