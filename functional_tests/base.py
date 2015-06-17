from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver

CHROME_DRIVER_LOCATION = '/Users/zeulb/Dropbox/Programming/TDDPython/chromedriver'

class FunctionalTest(StaticLiveServerTestCase):

	def setUp(self):
		self.browser = webdriver.Chrome(CHROME_DRIVER_LOCATION)
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()