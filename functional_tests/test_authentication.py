from .base import FunctionalTest

class TestAuthentication(FunctionalTest):

	def test_can_register(self):
		self.browser.get(self.live_server_url+'/account/register')
		username_input = self.browser.find_element_by_id('id_username')
		password1_input = self.browser.find_element_by_id('id_password1')
		password2_input = self.browser.find_element_by_id('id_password2')

		username_input.send_keys('anduk')
		password1_input.send_keys('budi')
		password2_input.send_keys('budi')

		self.browser.find_element_by_xpath('//input[@type="submit"]').click()

		self.assertNotEqual(self.browser.current_url, self.live_server_url+'/account/register')

	def test_cannot_register_with_different_password_confirmation(self):
		self.browser.get(self.live_server_url+'/account/register')
		username_input = self.browser.find_element_by_id('id_username')
		password1_input = self.browser.find_element_by_id('id_password1')
		password2_input = self.browser.find_element_by_id('id_password2')

		username_input.send_keys('anduk')
		password1_input.send_keys('budi')
		password2_input.send_keys('budi2')

		self.browser.find_element_by_xpath('//input[@type="submit"]').click()

		self.assertEqual(self.browser.current_url, self.live_server_url+'/account/register')

	def test_cannot_register_multiple_account(self):
		self.browser.get(self.live_server_url+'/account/register')
		username_input = self.browser.find_element_by_id('id_username')
		password1_input = self.browser.find_element_by_id('id_password1')
		password2_input = self.browser.find_element_by_id('id_password2')

		username_input.send_keys('anduk')
		password1_input.send_keys('budi')
		password2_input.send_keys('budi')

		self.browser.find_element_by_xpath('//input[@type="submit"]').click()

		self.browser.get(self.live_server_url+'/account/register')
		username_input = self.browser.find_element_by_id('id_username')
		password1_input = self.browser.find_element_by_id('id_password1')
		password2_input = self.browser.find_element_by_id('id_password2')

		username_input.send_keys('anduk')
		password1_input.send_keys('budi')
		password2_input.send_keys('budi')

		self.browser.find_element_by_xpath('//input[@type="submit"]').click()

		self.assertEqual(self.browser.current_url, self.live_server_url+'/account/register')
