from .base import FunctionalTest

class TestAuthentication(FunctionalTest):

	def register_user(self, username, password1, password2):
		self.browser.get(self.live_server_url+'/account/register')
		username_input = self.browser.find_element_by_id('id_username')
		password1_input = self.browser.find_element_by_id('id_password1')
		password2_input = self.browser.find_element_by_id('id_password2')

		username_input.send_keys(username)
		password1_input.send_keys(password1)
		password2_input.send_keys(password2)

		self.browser.find_element_by_xpath('//input[@type="submit"]').click()

	def login_user(self, username, password):
		self.browser.get(self.live_server_url+'/account/login')
		username_input = self.browser.find_element_by_id('id_username')
		password_input = self.browser.find_element_by_id('id_password')

		username_input.send_keys(username)
		password_input.send_keys(password)

		self.browser.find_element_by_xpath('//input[@type="submit"]').click()


	def test_can_register(self):
		self.register_user('anduk', 'budi', 'budi')

		self.assertNotEqual(self.browser.current_url, self.live_server_url+'/account/register')

	def test_cannot_register_with_different_password_confirmation(self):
		self.register_user('anduk', 'budi', 'budi2')

		self.assertEqual(self.browser.current_url, self.live_server_url+'/account/register')

	def test_cannot_register_multiple_account(self):
		self.register_user('anduk', 'budi', 'budi')

		self.register_user('anduk', 'budi', 'budi')

		self.assertEqual(self.browser.current_url, self.live_server_url+'/account/register')

	def test_can_login(self):
		self.register_user('budi', 'anduk', 'anduk')

		self.login_user('budi', 'anduk')

		self.assertNotEqual(self.browser.current_url, self.live_server_url+'/account/login')

	def test_cannot_login_with_wrong_password(self):
		self.register_user('budi', 'anduk', 'anduk')

		self.login_user('budi', 'andukk')

		self.assertEqual(self.browser.current_url, self.live_server_url+'/account/login')



