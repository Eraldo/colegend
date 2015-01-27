import datetime
from allauth.account.signals import user_signed_up
from django.contrib.messages import get_messages
from django.contrib.messages.storage.fallback import FallbackStorage
from django.core import mail
from django.db import IntegrityError
from django.test import TestCase, RequestFactory
from users.models import User
from users.tests.factories import UserFactory, ProfileFactory, ContactFactory, SettingsFactory


class UserModelTests(TestCase):
    def setUp(self):
        self.user_data = {
            "username": "Usernew", "password": "usernew",
        }

    def test_user_creation(self):
        """Test the creation of a new user."""
        User.objects.create_user(**self.user_data)
        user = User.objects.get(username=self.user_data["username"])
        self.assertEquals(user.check_password(self.user_data["password"]), True)

    def test_username_taken(self):
        """Test the creation of a user with a username that is already taken."""
        User.objects.create_user(**self.user_data)
        self.assertRaises(
            IntegrityError,
            User.objects.create_user,
            **self.user_data
        )

    def test_username_missing(self):
        """Test the creation of a user without the required username field."""
        data = self.user_data
        data.pop("username")
        self.assertRaises(
            TypeError,
            User.objects.create_user,
            **data
        )

    def test_password_missing(self):
        """Test the creation of a user without the password. A random password should be chosen."""
        data = self.user_data
        data.pop("password")
        User.objects.create_user(**data)
        user = User.objects.get(username="Usernew")
        self.assertEquals(len(user.password), 41)

    def test_get_name(self):
        """Test the retrieval of the user's name."""
        data = self.user_data
        data["first_name"] = "FirstName"
        data["last_name"] = "LastName"
        User.objects.create_user(**data)
        user = User.objects.get(username=data["username"])
        self.assertEquals(user.get_name(), "FirstName LastName")

    def test_get_short_name(self):
        user = UserFactory()
        self.assertEqual(user.get_short_name(), user.first_name)

    def test_get_full_name(self):
        user = UserFactory()
        self.assertEqual(user.get_full_name(), "Joe Doe")

    def test_is_accepted(self):
        """Test the user property: default, get, set."""
        User.objects.create_user(**self.user_data)
        user = User.objects.get(username=self.user_data["username"])
        # Test getter
        self.assertIsNotNone(user.is_accepted)
        # Make sure that a new user is not accepted by default.
        self.assertFalse(user.is_accepted)
        # Test setter
        user.is_accepted = True
        self.assertTrue(user.is_accepted)

    def test_accept(self):
        User.objects.create_user(**self.user_data)
        user = User.objects.get(username=self.user_data["username"])
        user.accept()

        # Check if the acceptance flag was set.
        self.assertTrue(user.is_accepted)

    def test_accept_email(self):
        User.objects.create_user(**self.user_data)
        user = User.objects.get(username=self.user_data["username"])
        user.accept()

        self.assertEquals(len(mail.outbox), 1)
        self.assertEquals(mail.outbox[0].subject, '[CoLegend] Account verified!')

    def test_create_multiple_users(self):
        UserFactory(first_name="a")
        UserFactory(first_name="b")
        UserFactory(first_name="c")
        self.assertEqual(User.objects.count(), 3)

    # test URLs

    def test_get_show_url(self):
        user = UserFactory()
        self.assertEqual(user.get_show_url(), "/users/joedoe/")

    # test QuerySets

    def test_get_pending_users(self):
        user1 = UserFactory()
        user2 = UserFactory(first_name="Joe2", is_accepted=False)
        pending_users = User.objects.pending()
        self.assertEqual(pending_users.count(), 1)
        self.assertTrue(user2 in pending_users)
        self.assertFalse(user1 in pending_users)

    def test_get_accepted_users(self):
        user1 = UserFactory(first_name="Joe1")
        user2 = UserFactory(first_name="Joe2", is_accepted=False)
        accepted_users = User.objects.accepted()
        self.assertEqual(accepted_users.count(), 1)
        self.assertTrue(user1 in accepted_users)
        self.assertFalse(user2 in accepted_users)

    def test_get_users_projects(self):
        user = UserFactory()
        self.assertEqual(user.projects.count(), 0)

    def test_get_users_tasks(self):
        user = UserFactory()
        self.assertEqual(user.tasks.count(), 0)

    def test_get_users_tags(self):
        user = UserFactory()
        self.assertEqual(user.tags.count(), 0)


class ContactModelTests(TestCase):
    def test_create_contact(self):
        contact = ContactFactory()
        self.assertEqual(str(contact), "Joe Doe (joedoe)")

    def test_first_name(self):
        contact = ContactFactory()
        self.assertEqual(contact.first_name, contact.owner.first_name)
        contact.first_name = "foo"
        self.assertEqual(contact.owner.first_name, "foo")

    def test_last_name(self):
        contact = ContactFactory()
        self.assertEqual(contact.last_name, contact.owner.last_name)
        contact.last_name = "bar"
        self.assertEqual(contact.owner.last_name, "bar")

    def test_email(self):
        contact = ContactFactory()
        self.assertEqual(contact.email, contact.owner.email)
        contact.email = "abc@example.com"
        self.assertEqual(contact.owner.email, "abc@example.com")

    def test_get_name(self):
        contact = ContactFactory()
        self.assertEqual(contact.get_name(), contact.owner.get_name())

    def test_get_gender_symbol(self):
        contact = ContactFactory()
        self.assertEqual(contact.get_gender_symbol(), "♂")

    def test_get_address(self):
        contact = ContactFactory()
        self.assertEqual(contact.get_address(), "Street 1\n12345 Linz\nAustria")

    def test_get_age(self):
        contact = ContactFactory()
        born = contact.birthday
        today = datetime.datetime.today()
        age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
        self.assertEqual(contact.get_age(), age)


class ProfileModelTests(TestCase):
    def test_profile_string(self):
        profile = ProfileFactory()
        self.assertEqual(str(profile), "{}'s Profile".format(profile.owner.username))


class SettingsModelTests(TestCase):
    def test_settings_string(self):
        settings = SettingsFactory()
        self.assertEqual(str(settings), "{}'s Settings".format(settings.owner.username))


class SignupNotificationTests(TestCase):

    def setUp(self):
        # prepare request for signal
        request = RequestFactory().get("/")
        setattr(request, 'session', 'session')
        messages = FallbackStorage(request)
        setattr(request, '_messages', messages)
        # send user_signed_up signal
        user_signed_up.send(sender=User, request=request, user=UserFactory())
        # add request to test class
        self.request = request

    def test_notify_user_after_signup(self):
        """check if user got a message"""
        messages = [m.message for m in get_messages(self.request)]
        self.assertIn("We have received your application.", messages)

    def test_notify_managers_after_signup(self):
        # check if managers got an email
        self.assertEquals(len(mail.outbox), 1)
        email = mail.outbox[0]
        self.assertEquals(email.subject, 'New user: joedoe')
        self.assertEquals(email.to, ['connect@colegend.org'])
