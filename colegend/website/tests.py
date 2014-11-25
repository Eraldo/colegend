from time import sleep
from unittest import skip
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

    @skip("TODO: fix to work with travis.")
    def test_login(self):
        tester = User.objects.create_user(username="Tester", password="tester")
        self.selenium.get('%s%s' % (self.live_server_url, '/accounts/login/'))
        username_input = self.selenium.find_element_by_name("login")
        username_input.send_keys(tester.username)
        # username_input.send_keys("tester")
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys("tester")
        self.selenium.find_element_by_name("login_submit").click()
        # sleep(20)
        # self.selenium.save_screenshot("/Users/eraldo/inbox/test.png")

    def test_can_view_admin_site(self):
        # Gertrude opens her web browser, and goes to the admin page
        self.selenium.get(self.live_server_url + '/backend/')

        # She sees the familiar 'Django administration' heading
        body = self.selenium.find_element_by_tag_name('body')
        self.assertIn('CoLegend backend', body.text)
