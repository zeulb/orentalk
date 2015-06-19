from .base import FunctionalTest


EMPTY_TITLE_ERROR = "You can't create a room with blank title"

class TestHomePage(FunctionalTest):

	def test_redirected_when_creating_new_chat_room(self):
		self.browser.get(self.live_server_url)

		current_url = self.browser.current_url
		
		new_chat_form = self.browser.find_element_by_id('id_title')
		new_chat_form.send_keys('Gajah terbang\n')

		new_url = self.browser.current_url

		self.assertNotEqual(current_url, new_url)

	def test_new_chat_room_contain_page_title(self):
		self.browser.get(self.live_server_url)
		
		new_chat_form = self.browser.find_element_by_id('id_title')
		new_chat_form.send_keys('Gajah terbang lagi\n')

		page_title = self.browser.find_element_by_id('page-title').text

		self.assertIn('Gajah terbang lagi', page_title)

	def test_error_message_on_creating_chat_room_with_blank_title(self):
		self.browser.get(self.live_server_url)
		
		new_chat_form = self.browser.find_element_by_id('id_title')
		new_chat_form.send_keys('\n')

		error_message = self.browser.find_element_by_class_name('has-error').text

		self.assertEqual(error_message, EMPTY_TITLE_ERROR)


