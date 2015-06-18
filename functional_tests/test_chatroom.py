from .base import FunctionalTest


EMPTY_TITLE_ERROR = "You can't create a room with blank title"

class TestChatRoom(FunctionalTest):
	
	def test_can_add_message_in_a_chat_room(self):
		self.browser.get(self.live_server_url)

		new_chat_form = self.browser.find_element_by_id('id_title')
		new_chat_form.send_keys('Budi makan gajah\n')

		new_message_form = self.browser.find_element_by_id('id_text')
		new_message_form.send_keys('Halo\n')

		self.assertContains(self.browser.page_source, 'Halo')

	def test_message_still_saved_after_refresh(self):
		self.browser.get(self.live_server_url)

		new_chat_form = self.browser.find_element_by_id('id_title')
		new_chat_form.send_keys('Budi makan gajah\n')

		new_message_form = self.browser.find_element_by_id('id_text')
		new_message_form.send_keys('Halo\n')
		
		self.browser.refresh()

		self.assertContains(self.browser.page_source, 'Halo')

	def test_can_send_more_than_one_message(self):
		self.browser.get(self.live_server_url)

		new_chat_form = self.browser.find_element_by_id('id_title')
		new_chat_form.send_keys('Budi makan gajah\n')

		new_message_form = self.browser.find_element_by_id('id_text')
		new_message_form.send_keys('Halo\n')

		new_message_form = self.browser.find_element_by_id('id_text')
		new_message_form.send_keys('Helo lagi\n')

		self.assertContains(self.browser.page_source, 'Halo')
		self.assertContains(self.browser.page_source, 'Helo lagi')
