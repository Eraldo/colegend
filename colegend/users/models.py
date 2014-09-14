from annoying.fields import AutoOneToOneField
from django.contrib import messages
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser
from django.core import validators
from django.core.validators import MaxValueValidator
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.core.mail import send_mail, mail_managers
from django.db import models
from lib.modelfields import PhoneField
from users.modelfields import RequiredBooleanField
from users.managers import UserManager

__author__ = 'eraldo'


class User(AbstractBaseUser, PermissionsMixin):
    """
    Fully featured User model with admin-compliant permissions.

    Username and password are required. Other fields are optional.
    """
    username = models.CharField(_('username'), max_length=30, unique=True,
                                help_text=_('Required. 30 characters or fewer. Letters, digits and '
                                            '@/./+/-/_ only.'),
                                validators=[
                                    validators.RegexValidator(r'^[\w.@+-]+$', _('Enter a valid username.'), 'invalid')
                                ])
    email = models.EmailField(_('email address'), blank=True)

    # > contact
    # > profile

    @property
    def first_name(self):
        try:
            return self.contact.first_name
        except Contact.DoesNotExist:
            return ""

    @first_name.setter
    def first_name(self, value):
        self.contact.first_name = value

    @property
    def last_name(self):
        try:
            return self.contact.last_name
        except Contact.DoesNotExist:
            return ""

    @last_name.setter
    def last_name(self, value):
        self.contact.last_name = value

    # Roles

    is_active = models.BooleanField(verbose_name=_('active'), default=True,
                                    help_text=_('Designates whether this user should be treated as '
                                                'active. Unselect this instead of deleting accounts.'))
    is_accepted = models.BooleanField(verbose_name=_('accepted'), default=False,
                                      help_text="Designates whether the user has been accepted by the site managers.")

    is_tester = models.BooleanField(verbose_name=_('tester'), default=False,
                                    help_text="Designates whether the user can access the site's test features.")

    is_staff = models.BooleanField(verbose_name=_('staff'), default=False,
                                   help_text=_('Designates whether the user can log into this admin '
                                               'site.'))

    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        if self.contact:
            return self.contact.name
        else:
            return self.username

    get_full_name.short_description = 'Name'

    def get_short_name(self):
        "Returns the short name for the user."
        if self.contact:
            return self.contact.first_name
        else:
            return self.username

    get_short_name.short_description = 'Short name'

    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email], **kwargs)

    # As of Django 1.8 this will be fixed by using "default_related_name" in the respective model's Meta class.
    # https://docs.djangoproject.com/en/dev/ref/models/options/#default-related-name
    # example: http://gitelephant.cypresslab.net/django/commit/87d0a3384cc263fe0df749a28e2fbc1e1240f043
    @property
    def projects(self):
        return self.project_set

    @property
    def tasks(self):
        return self.task_set

    @property
    def tags(self):
        return self.tag_set


from allauth.account.signals import user_signed_up
from django.dispatch import receiver


@receiver(user_signed_up, dispatch_uid="notify_managers_after_signup")
def notify_managers_after_signup(request, user, **kwargs):
    """
    Inform the admin that a new user has signed up for the system.

    :param request:
    :param user:
    :param kwargs:
    """

    # Notify the managers.
    mail_managers(
        subject="New user: {}".format(user),
        message="A new user has signed up:\nUsername: {}\nEmail: {}".format(user, user.email),
        fail_silently=True
    )
    messages.add_message(request, messages.SUCCESS, 'We have received your application.')


class Contact(models.Model):
    user = models.OneToOneField(User)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    GENDER_CHOICES = (
        ('M', 'Male Legend ♂'),
        ('F', 'Female Legend ♀'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    birthday = models.DateField()

    email = models.EmailField()

    @property
    def email(self):
        if self.user:
            return self.user.email
        else:
            return ""

    @email.setter
    def email(self, value):
        if self.user:
            self.user.email = value
        else:
            raise User.DoesNotExist

    phone_number = PhoneField(help_text="Mobile or other phone number. Example: +4369910203039")

    street = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=5)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    @property
    def name(self):
        return "{} {}".format(self.first_name, self.last_name)

    def __str__(self):
        if self.user:
            user = self.user
        else:
            user = "Unknown"
        return "{} ({})".format(self.name, user)


class Profile(models.Model):
    """
    A user signup application model.
    This is used to get and save some information about the user upon account signup.
    """
    user = models.OneToOneField(User)

    # QUESTIONS
    origin = models.TextField(
        verbose_name="How did you get to know CoLegend?",
        help_text="Talking with someone? Internet search? Other source/medium?"
    )
    referrer = models.CharField(
        verbose_name="Contact Person",
        max_length=30,
        help_text="If a person introduced you to CoLegend.. please mention his/her/their name here.",
        blank=True, null=True
    )
    experience = models.TextField(
        verbose_name="Do you have prior Personal Development Experience?",
        help_text="Seminars? Workshops? Education? Books? etc"
    )
    motivation = models.TextField(
        verbose_name="What is your motivation to join this platform?",
    )
    change = models.TextField(
        verbose_name="What do you want to change in your life?",
        help_text="Possible topics could be: home, relationships, work, purpose, self, etc."
    )
    drive = models.PositiveIntegerField(
        verbose_name="How strong is your drive/willingness to change yourself to get there?",
        help_text="1 = very low, 10 = very high",
    )
    expectations = models.TextField(
        verbose_name="What are your expectations of this platform?",
        help_text="What do you think or wish the platform can do for you?"
    )
    other = models.TextField(
        verbose_name="Anything else you want to share?",
        blank=True, null=True
    )

    # GUIDELINES
    YES_OR_NO = (
        (True, 'Yes'),
        (False, 'No')
    )
    stop = RequiredBooleanField(
        verbose_name="Stop Rule",
        help_text="When someone says 'stop' it means stop!",
        default=False
    )
    discretion = RequiredBooleanField(
        help_text="Everything stays in the CoLegend World.",
        default=False
    )
    responsibility = RequiredBooleanField(
        verbose_name="Individual Responsibility",
        help_text="I am responsible for my own experience.",
        default=False
    )
    appreciation = RequiredBooleanField(
        help_text="I am willing to treat the Platform and its members with appreciation.",
        default=False
    )
    terms = RequiredBooleanField(
        verbose_name="Terms and Conditions",
        help_text="I accept the general advice, terms and conditions.",
        default=False
    )

    def __str__(self):
        if self.user:
            user = self.user
        else:
            user = "Unknown"
        return "{}'s Profile".format(user)


class Settings(models.Model):
    owner = AutoOneToOneField(User, primary_key=True)
    # ISO 639-1
    ENGLISH = "EN"
    LANGUAGE_CHOICES = (
        (ENGLISH, 'English'),
    )
    language = models.CharField(max_length=2,
                                choices=LANGUAGE_CHOICES,
                                default=ENGLISH)
    day_start = models.PositiveSmallIntegerField(
        verbose_name="Day start time", default=0,
        help_text="When does your day start? Enter number between 0 and 24 (24h clock).",
        validators=[MaxValueValidator(24)])
    sound = models.BooleanField(verbose_name="Sound enabled", default=True)

    class Meta:
        verbose_name_plural = "Settings"

    def __str__(self):
        return "{}'s Settings".format(self.owner)
