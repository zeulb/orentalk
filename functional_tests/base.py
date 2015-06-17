from django.test import LiveServerTestCase
from selenium import webdriver

CHROME_DRIVER_LOCATION = '/Users/zeulb/Dropbox/Programming/TDDPython/chromedriver'

class FunctionalTest(LiveServerTestCase):

	def setUp(self):
		self.browser = webdriver.Chrome(CHROME_DRIVER_LOCATION)

	def tearDown(self):
		self.browser.quit()