from .base import FunctionalTest

class TestAuthentication(FunctionalTest):

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



