from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser, UserManager
from django.core import validators
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.core.mail import send_mail, mail_managers
from django.db import models
from lib.modelfields import PhoneField
from users.modelfields import RequiredBooleanField

__author__ = 'eraldo'


class Contact(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    GENDER_CHOICES = (
        ('M', 'Male Legend ♂'),
        ('F', 'Female Legend ♀'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    birthday = models.DateField()

    email = models.EmailField()
    phone_number = PhoneField(help_text="Mobile or other phone number. Example: +4369910203039")

    street = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=5)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    # @property
    # def user(self):
    #     try:
    #         return self.user
    #     except User.DoesNotExist as e:
    #         return None


    @property
    def name(self):
        return "{} {}".format(self.first_name, self.last_name)

    def __str__(self):
        try:
            user = self.user
        except User.DoesNotExist:
            user = "Unknown"
        return "{} ({})".format(self.name, user)


class Profile(models.Model):
    """
    A user signup application model.
    This is used to get and save some information about the user upon account signup.
    """
    # > owner
    # > questions

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
        try:
            user = self.user
        except User.DoesNotExist:
            user = "Unknown"
        return "{}'s Profile".format(user)


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

    @property
    def first_name(self):
        if self.contact:
            return self.contact.first_name
        else:
            return ""

    @first_name.setter
    def first_name(self, value):
        self.contact.first_name = value

    @property
    def last_name(self):
        if self.contact:
            return self.contact.last_name
        else:
            return ""

    @last_name.setter
    def last_name(self, value):
        self.contact.last_name = value

    @property
    def email(self):
        if self.contact:
            return self.contact.email
        else:
            return ""

    @email.setter
    def email(self, value):
        self.contact.email = value


    is_staff = models.BooleanField(_('staff status'), default=False,
        help_text=_('Designates whether the user can log into this admin '
                    'site.'))
    is_active = models.BooleanField(_('active'), default=False,
        help_text=_('Designates whether this user should be treated as '
                    'active. Unselect this instead of deleting accounts.'))

    is_tester = models.BooleanField(verbose_name="tester status", default=False,
                                    help_text="Designates whether the user can access the site's test features.")

    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    contact = models.OneToOneField(Contact, null=True)
    profile = models.OneToOneField(Profile, null=True)
    # Roles

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __init__(self, *args, **kwargs):

        super(User, self).__init__(*args, **kwargs)

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        if self.contact:
            return self.contact.name
        else:
            return self.username

    def get_short_name(self):
        "Returns the short name for the user."
        if self.contact:
            return self.contact.first_name
        else:
            return self.username

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
