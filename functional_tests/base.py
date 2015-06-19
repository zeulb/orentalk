from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver

CHROME_DRIVER_LOCATION = '/Users/zeulb/Dropbox/Programming/TDDPython/chromedriver'

class FunctionalTest(StaticLiveServerTestCase):

	def setUp(self):
		self.browser = webdriver.Chrome(CHROME_DRIVER_LOCATION)
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

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