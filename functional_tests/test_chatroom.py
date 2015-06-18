from .base import FunctionalTest

class TestChatRoom(FunctionalTest):

	def test_can_add_message_in_a_chat_room(self):
		self.browser.get(self.live_server_url)

		new_chat_form = self.browser.find_element_by_id('id_title')
		new_chat_form.send_keys('Budi makan gajah\n')

		new_message_form = self.browser.find_element_by_id('id_text')
		new_message_form.send_keys('Halo\n')


		self.assertIn('Halo', self.browser.page_source)

	def test_message_still_saved_after_refresh(self):
		self.browser.get(self.live_server_url)

		new_chat_form = self.browser.find_element_by_id('id_title')
		new_chat_form.send_keys('Budi makan gajah\n')

		new_message_form = self.browser.find_element_by_id('id_text')
		new_message_form.send_keys('Halo\n')
		
		self.browser.refresh()

		self.assertIn('Halo', self.browser.page_source)

	def test_can_send_more_than_one_message(self):
		self.browser.get(self.live_server_url)

		new_chat_form = self.browser.find_element_by_id('id_title')
		new_chat_form.send_keys('Budi makan gajah\n')

		new_message_form = self.browser.find_element_by_id('id_text')
		new_message_form.send_keys('Halo\n')

		new_message_form = self.browser.find_element_by_id('id_text')
		new_message_form.send_keys('Helo lagi\n')

		self.assertIn('Halo', self.browser.page_source,)
		self.assertIn('Helo lagi', self.browser.page_source)
