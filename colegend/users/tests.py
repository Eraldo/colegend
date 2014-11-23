import datetime
from unittest import mock
from allauth.account.signals import user_signed_up
from django.contrib.messages import get_messages
from django.contrib.messages.storage.fallback import FallbackStorage
from django.core import mail
from django.core.urlresolvers import reverse
from django.db import IntegrityError
from django.http import HttpRequest
from django.test import TestCase, RequestFactory
import factory
from users.models import User, Contact, Profile, Settings


class UserFactory(factory.DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create = ('username',)

    first_name = "John"
    last_name = "Doe"
    username = factory.LazyAttribute(lambda a: '{0}{1}'.format(a.first_name, a.last_name).lower())
    password = factory.PostGenerationMethodCall('set_password', 'tester')
    email = factory.LazyAttribute(lambda a: '{0}@example.com'.format(a.username).lower())
    is_accepted = True


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
        self.assertEqual(user.get_full_name(), "John Doe")

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
        self.assertEqual(user.get_show_url(), "/users/johndoe/")

    # test QuerySets

    def test_get_pending_users(self):
        user1 = UserFactory()
        user2 = UserFactory(first_name="John2", is_accepted=False)
        pending_users = User.objects.pending()
        self.assertEqual(pending_users.count(), 1)
        self.assertTrue(user2 in pending_users)
        self.assertFalse(user1 in pending_users)

    def test_get_accepted_users(self):
        user1 = UserFactory()
        user2 = UserFactory(first_name="John2", is_accepted=False)
        accepted_users = User.objects.accepted()
        self.assertEqual(accepted_users.count(), 1)
        self.assertTrue(user1 in accepted_users)
        self.assertFalse(user2 in accepted_users)


class UserViewTests(TestCase):
    def test_list_view_anonymous(self):
        response = self.client.get(reverse('users:list'))
        self.assertEquals(response.status_code, 302)

    def test_list_view_authenticated(self):
        """Test the user list view with a logged in user."""
        usernew = User.objects.create_user(username="Usernew", password="usernew", is_accepted=True)
        self.client.login(username="Usernew", password="usernew")
        response = self.client.get(reverse('users:list'))
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, "Usernew")
        self.assertQuerysetEqual(response.context['user_list'], ['<User: Usernew>'])

    def test_list_view_unauthenticated(self):
        """Test the user list view with a logged in user."""
        usernew = User.objects.create_user(username="Usernew", password="usernew", is_accepted=False)
        self.client.login(username="Usernew", password="usernew")
        response = self.client.get(reverse('users:list'))
        self.assertEquals(response.status_code, 302)


class ContactFactory(factory.DjangoModelFactory):
    class Meta:
        model = Contact
        django_get_or_create = ('owner',)

    owner = factory.SubFactory(UserFactory)
    phone_number = "+4369910203039"
    street = "Street 1"
    postal_code = "12345"
    city = "Linz"
    country = "Austria"
    gender = "M"
    birthday = datetime.date(1985, 4, 4)


class ContactModelTests(TestCase):
    def test_create_contact(self):
        contact = ContactFactory()
        self.assertEqual(str(contact), "John Doe (johndoe)")

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


class ProfileFactory(factory.DjangoModelFactory):
    class Meta:
        model = Profile
        django_get_or_create = ('owner',)

    owner = factory.SubFactory(UserFactory)
    origin = "some origin"
    referrer = "some referrer"
    experience = "some experience"
    motivation = "some motivation"
    change = "some change"
    drive = 6
    expectations = "some expectations"
    other = "some other"
    stop = True
    discretion = True
    responsibility = True
    appreciation = True
    terms = True


class ProfileModelTests(TestCase):
    def test_profile_string(self):
        profile = ProfileFactory()
        self.assertEqual(str(profile), "johndoe's Profile")


class SettingsFactory(factory.DjangoModelFactory):
    class Meta:
        model = Settings
        django_get_or_create = ('owner',)

    owner = factory.SubFactory(UserFactory)
    language = "EN"
    journal_entry_template = "some journal entry template"


class SettingsModelTests(TestCase):
    def test_settings_string(self):
        settings = SettingsFactory()
        self.assertEqual(str(settings), "johndoe's Settings")


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
        self.assertEquals(email.subject, '[Django] New user: johndoe')
        self.assertEquals(email.to, ['eraldo@eraldo.org'])
