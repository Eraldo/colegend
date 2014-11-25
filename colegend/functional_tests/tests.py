from unittest import skip
from django.test import LiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
from users.tests import UserFactory

__author__ = 'eraldo'


class ViewTests(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        cls.browser = WebDriver()
        super().setUpClass()

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        super().tearDownClass()

    def setUp(self):
        self.user = UserFactory(is_superuser=True, is_staff=True)

    def test_login(self):
        browser = self.browser
        # navigate to the home page
        browser.get('%s%s' % (self.live_server_url, '/'))
        # click on the login button
        browser.find_element_by_id("login-button").click()
        # enter credentials
        username_input = browser.find_element_by_name("login")
        username_input.send_keys(self.user.username)
        password_input = browser.find_element_by_name("password")
        password_input.send_keys("tester")
        # sign in
        browser.find_element_by_name("login_submit").click()
        # check title
        self.assertIn("Welcome", browser.title)

    @skip("TODO: Write test.")
    def test_signup(self):
        self.fail()

    def test_can_view_admin_site(self):
        # Gertrude opens her web browser, and goes to the admin page
        self.browser.get(self.live_server_url + '/backend/')
        # She sees the familiar 'Django administration' heading
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('CoLegend backend', body.text)
