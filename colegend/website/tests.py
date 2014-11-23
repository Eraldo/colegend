from time import sleep
from django.test import TestCase
from django.test import LiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
from users.models import User


class ViewTests(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        cls.selenium = WebDriver()
        super(ViewTests, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(ViewTests, cls).tearDownClass()

    def test_login(self):
        tester = User.objects.create_user(username="Tester", password="tester")
        self.selenium.get('%s%s' % (self.live_server_url, '/accounts/login/'))
        username_input = self.selenium.find_element_by_name("login")
        username_input.send_keys(tester.username)
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys("tester")
        self.selenium.find_element_by_name("login_submit").click()
        # sleep(20)
        # self.selenium.save_screenshot("/Users/eraldo/inbox/test.png")
