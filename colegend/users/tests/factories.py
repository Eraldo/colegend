import datetime
import factory
from users.models import User, Contact, Profile, Settings

__author__ = 'eraldo'


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

    @factory.post_generation
    def confirm_email(self, create, extracted, **kwargs):
        """
        Automatically verify the user's email address.

        Verification takes place if the object is created:
        Example: UserFactory(...) or UserFactory.create(...)

        Verification does not take place if the object is created with this attribute set to False:
        Example: UserFactory(confirm_email=False)
        """
        if create and not extracted is False:
            self.emailaddress_set.add_email(None, self, self.email)
            email_obj = self.emailaddress_set.first()
            email_obj.verified = True
            email_obj.set_as_primary(conditional=True)


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


class SettingsFactory(factory.DjangoModelFactory):
    class Meta:
        model = Settings
        django_get_or_create = ('owner',)

    owner = factory.SubFactory(UserFactory)
    language = "EN"
    journal_entry_template = "some journal entry template"
