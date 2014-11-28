from time import sleep
from unittest import skip
from django.core.urlresolvers import reverse
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

    def test_signup(self):
        browser = self.browser
        # John opens his browser and goes to the login page.
        browser.get(self.live_server_url + reverse("account_login"))
        # He clicks clicks on the area which says "Nope, I am new here ..."
        browser.find_element_by_id("signup_choice").click()
        # He clicks clicks on the button which says "How can I join?"
        browser.find_element_by_id("signup").click()
        # He enters his personal data..
        browser.find_element_by_id("id_username").send_keys("newuser")
        browser.find_element_by_id("id_origin").send_keys("some origin")
        browser.find_element_by_id("id_referrer").send_keys("some referrer")
        browser.find_element_by_id("id_experience").send_keys("some experience")
        browser.find_element_by_id("id_motivation").send_keys("some motivation")
        browser.find_element_by_id("id_change").send_keys("some change")
        browser.find_element_by_id("id_drive").send_keys("8")
        browser.find_element_by_id("id_expectations").send_keys("some expectations")
        browser.find_element_by_id("id_other").send_keys("some other")
        browser.find_element_by_id("id_stop").click()
        browser.find_element_by_id("id_discretion").click()
        browser.find_element_by_id("id_responsibility").click()
        browser.find_element_by_id("id_appreciation").click()
        browser.find_element_by_id("id_terms").click()
        browser.find_element_by_id("id_first_name").send_keys("FirstName")
        browser.find_element_by_id("id_last_name").send_keys("LastName")
        browser.find_element_by_id("id_gender").send_keys("M")
        browser.find_element_by_id("id_birthday").send_keys("1994-01-01")
        browser.find_element_by_id("id_email").send_keys("newuser@example.com")
        browser.find_element_by_id("id_phone_number").send_keys("+1234567890")
        browser.find_element_by_id("id_street").send_keys("Some Street 1")
        browser.find_element_by_id("id_postal_code").send_keys("12345")
        browser.find_element_by_id("id_city").send_keys("Some City")
        browser.find_element_by_id("id_country").send_keys("Some Country")
        browser.find_element_by_id("id_password1").send_keys("somepassword")
        browser.find_element_by_id("id_password2").send_keys("somepassword")
        # He sends his application.
        browser.find_element_by_id("submit-id-save").click()
        # He is prompted to verify his e-mail address.
        self.assertEqual("Verify Your E-mail Address", browser.title)

    def test_can_view_admin_site(self):
        # Gertrude opens her web browser, and goes to the admin page
        self.browser.get(self.live_server_url + '/backend/')
        # She sees the familiar 'CoLegend backend' heading
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('CoLegend backend', body.text)
