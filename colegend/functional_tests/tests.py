from django.core import mail
from django.core.urlresolvers import reverse
from django.test import LiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
from users.tests.test_models import UserFactory

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

    def login_user(self, username, password):
        browser = self.browser
        browser.get(self.live_server_url + '/')

        ## The user clicks on the login button.
        browser.find_element_by_id("login-button").click()

        ## He enters credentials.
        username_input = browser.find_element_by_name("login")
        username_input.send_keys(username)
        password_input = browser.find_element_by_name("password")
        password_input.send_keys(password)

        ## He clicks to sign in.
        browser.find_element_by_name("login_submit").click()

    def logout_user(self):
        browser = self.browser

        ## The user goes to the logout page.
        browser.get(self.live_server_url + reverse("account_logout"))
        self.assertEqual("Sign Out", browser.title)

        ## He logs out.
        browser.find_element_by_id("sign_out").click()

        ## The user is taken back to the CoLegend about page.
        self.assertEqual("CoLegend", browser.title)

    def test_login(self):
        browser = self.browser

        ## The user logs in.
        self.login_user(self.user.username, "tester")

        ## He lands on the welcome page.
        self.assertIn("Welcome", browser.title)

    def test_signup(self):
        browser = self.browser

        ## Max opens his browser and goes to the login page.
        browser.get(self.live_server_url + reverse("account_login"))
        browser.maximize_window()

        ## He clicks clicks on the area which says "Nope, I am new here ..."
        browser.find_element_by_id("signup_choice").click()

        ## He clicks clicks on the button which says "How can I join?"
        browser.find_element_by_id("signup").click()

        # Preparing data for Max.
        new_user = {
            "username": "maxdoe",
            "password": "somepassword",
            "email": "newuser@example.com"
        }

        ## He starts with his username and motivational context.
        browser.find_element_by_id("id_username").send_keys(new_user.get("username"))
        browser.find_element_by_id("id_origin").send_keys("some origin")
        browser.find_element_by_id("id_referrer").send_keys("some referrer")
        browser.find_element_by_id("id_experience").send_keys("some experience")
        browser.find_element_by_id("id_motivation").send_keys("some motivation")
        browser.find_element_by_id("id_change").send_keys("some change")
        browser.find_element_by_id("id_drive").send_keys("8")
        browser.find_element_by_id("id_expectations").send_keys("some expectations")
        browser.find_element_by_id("id_other").send_keys("some other")

        ## Max agrees to the guidelines.
        browser.find_element_by_id("id_stop").click()
        browser.find_element_by_id("id_discretion").click()
        browser.find_element_by_id("id_responsibility").click()
        browser.find_element_by_id("id_appreciation").click()
        browser.find_element_by_id("id_terms").click()

        ## He enters his contact data.
        browser.find_element_by_id("id_first_name").send_keys("FirstName")
        browser.find_element_by_id("id_last_name").send_keys("LastName")
        browser.find_element_by_id("id_gender").send_keys("M")
        browser.find_element_by_id("id_birthday").send_keys("1994-01-01")
        browser.find_element_by_id("id_email").send_keys(new_user.get("email"))
        browser.find_element_by_id("id_phone_number").send_keys("+1234567890")
        browser.find_element_by_id("id_street").send_keys("Some Street 1")
        browser.find_element_by_id("id_postal_code").send_keys("12345")
        browser.find_element_by_id("id_city").send_keys("Some City")
        browser.find_element_by_id("id_country").send_keys("Some Country")

        ## He chooses a password.
        browser.find_element_by_id("id_password1").send_keys(new_user.get("password"))
        browser.find_element_by_id("id_password2").send_keys(new_user.get("password"))

        ## He sends his application.
        browser.find_element_by_id("submit-id-save").click()

        ## He is prompted to verify his e-mail address.
        self.assertEqual("Verify Your E-mail Address", browser.title)

        ## Max checks his email and finds one from CoLegend.
        self.assertEqual(len(mail.outbox), 2)  # One message for the user and one notification for the managers.
        activation_email = str(mail.outbox[1].message())

        ## He finds a line with an activation link starting with: "To confirm this is correct, go to <link>".
        found_lines = [line for line in activation_email.split("\n") if line.startswith("To confirm this is correct, go to ")]
        self.assertEqual(len(found_lines), 1)
        line = found_lines[0]
        confirmation_link = line.split(" go to ")[1]

        ## He starts his browser and navigates to the confirmation url.
        self.browser.get(confirmation_link)

        ## Max gets presented a page asking him to confirm his email address.
        self.assertEqual("Confirm E-mail Address", browser.title)

        ## He sees and clicks the confirmation button.
        browser.find_element_by_id("confirm_email").click()

        ## He now sees a page informing him that his application is getting processed.
        self.assertEqual("Processing Application", browser.title)

        ## Max signs out and waits for his verification as suggested.
        self.logout_user()

        ## A manager signs in and navigates to the user management page.
        manager = UserFactory(is_manager=True, username="hugodoe")
        browser.get(self.live_server_url + reverse("account_login"))

        ## Hugo logs in
        self.login_user(manager.username, "tester")

        ## Huge is now on his welcome page.
        self.assertIn("Welcome Hugodoe", browser.title)

        ## He clicks on the operator dropdown menu.
        browser.find_element_by_id("operator-menu").click()

        ## He clicks on the manage users sub-menu.
        browser.find_element_by_id("users-menu-item").click()

        ## He sees a pending user and clicks on the link.
        browser.find_element_by_id("pending-user-{}".format(new_user.get("username"))).click()

        ## He sees the users application details.
        # He searches for Max's email and contacts him to talk about the application.
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn(new_user.get("email"), body.text)

        ## He verifies the new user. (Max)
        browser.find_element_by_id("verify-pending-user").click()
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn("maxdoe is now verified.", body.text)

        ## Hugo logs out.
        self.logout_user()

        ## Max signs back in.
        self.login_user(new_user.get("username"), new_user.get("password"))

        ## Max is not verified and gets presented with his personal home view.
        self.assertEqual("Welcome Maxdoe", browser.title)

    def test_can_view_admin_site(self):

        ## Gertrude opens her web browser, and goes to the admin page.
        self.browser.get(self.live_server_url + '/backend/')

        ## She sees the familiar 'CoLegend backend' heading.
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('CoLegend backend', body.text)
