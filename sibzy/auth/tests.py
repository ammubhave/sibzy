from django.test import TestCase, LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from django.conf import settings
from auth.models import User, UserProfile
from django.core.urlresolvers import reverse
from django.core import management
import facebook

import os
os.environ['DJANGO_LIVE_TEST_SERVER_ADDRESS'] = 'localhost:8000'
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

        management.call_command('initdb')
    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        super(LoginTest, cls).tearDownClass()

    def test_fb_login(self):
        """
        Tests if the test user is able to login through facebook
        """
        #print self.fb_testuser
        self.browser.get(self.fb_testuser['login_url'])
        self.browser.get(self.fb_testuser['login_url'])
        self.browser.get(self.live_server_url + '/')

        # Wait for the page to reload aand login the user on the server side.
        WebDriverWait(self.browser, 10).until(lambda browser: 'fbid' in [cookie['name'] for cookie in browser.get_cookies()] and self.fb_testuser['id'] in [cookie['value'] for cookie in browser.get_cookies() if cookie['name'] == 'fbid'])

        assert len(User.objects.filter(username=self.fb_testuser['id'])) > 0
        assert len(UserProfile.objects.filter(fbid=self.fb_testuser['id'])) > 0

    def test_fb_logout_and_relogin(self):
        self.browser.find_element(By.CSS_SELECTOR, '[data-cid="btn-navbar-logout"]').click()

        WebDriverWait(self.browser, 10).until(lambda browser: 'fbid' not in [cookie['name'] for cookie in browser.get_cookies()])
