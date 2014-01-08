"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase, LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from django.conf import settings
from auth.models import User, UserProfile
import facebook


class LoginTest(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super(LoginTest, cls).setUpClass()
        cls.browser = webdriver.Firefox()
        cls.browser.implicitly_wait(5)

        # Create facebook test user
        cls.access_token = facebook.get_app_access_token(settings.FB_APPID, settings.FB_APPSECRET)
        graph = facebook.GraphAPI(cls.access_token)
        cls.fb_testuser = graph.request(settings.FB_APPID + '/accounts/test-users')['data'][0]

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        super(LoginTest, cls).tearDownClass()

    def test_fb_login(self):
        """
        Tests if the test user is able to login through facebook
        """
        print self.fb_testuser['login_url']
        self.browser.get(self.fb_testuser['login_url'])
        self.browser.get(self.fb_testuser['login_url'])
        self.browser.get(self.live_server_url + '/')

        WebDriverWait(self.browser, 100).until(lambda browser: 'fbid' in browser.get_cookies() and browser.get_cookies()['fbid'] != '')

