from time import sleep
from unittest import skip
from django.test import LiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
from users.models import User
from users.tests import UserFactory


class ViewTests(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        cls.selenium = WebDriver()
        super(ViewTests, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(ViewTests, cls).tearDownClass()

    def setUp(self):
        self.user = UserFactory(is_superuser=True, is_staff=True)

    # @skip("TODO: fix to work with travis.")
    def test_login(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/accounts/login/'))
        username_input = self.selenium.find_element_by_name("login")
        username_input.send_keys(self.user.username)
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys("tester")
        self.selenium.find_element_by_name("login_submit").click()
        sleep(20)

    def test_can_view_admin_site(self):
        # Gertrude opens her web browser, and goes to the admin page
        self.selenium.get(self.live_server_url + '/backend/')
        # She sees the familiar 'Django administration' heading
        body = self.selenium.find_element_by_tag_name('body')
        self.assertIn('CoLegend backend', body.text)
