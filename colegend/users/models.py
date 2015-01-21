from annoying.fields import AutoOneToOneField
from django.contrib import messages
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser
from django.core import validators
from django.core.urlresolvers import reverse
from django.core.validators import MaxValueValidator
from django.db.models import QuerySet
from django.template.loader import render_to_string
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.core.mail import send_mail, mail_managers
from django.db import models
from lib.modelfields import PhoneField
from users.modelfields import RequiredBooleanField
from users.managers import UserManager

__author__ = 'eraldo'


class UserQuerySet(QuerySet):
    def accepted(self):
        return self.filter(is_accepted=True)

    def pending(self):
        return self.filter(is_accepted=False)

    def managers(self):
        return self.filter(is_manager=True)


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
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)

    email = models.EmailField(_('email address'), blank=True)
    notes = models.TextField(
        help_text="Notes about this user.",
        blank=True
    )

    # > contact
    # > profile

    # Roles

    is_active = models.BooleanField(verbose_name=_('active'), default=True,
                                    help_text=_('Designates whether this user should be treated as '
                                                'active. Unselect this instead of deleting accounts.'))
    is_accepted = models.BooleanField(verbose_name=_('accepted'), default=False,
                                      help_text="Designates whether the user has been accepted by the site managers.")

    is_tester = models.BooleanField(verbose_name=_('tester'), default=False,
                                    help_text="Designates whether the user can access the site's test features.")

    is_manager = models.BooleanField(verbose_name=_('manager'), default=False,
                                     help_text="Designates whether the user can access the site's management features.")

    is_staff = models.BooleanField(verbose_name=_('staff'), default=False,
                                   help_text=_('Designates whether the user can log into this admin '
                                               'site.'))

    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    date_accepted = models.DateTimeField(_('date accepted'), null=True, blank=True)

    objects = UserManager.from_queryset(UserQuerySet)()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        return "{} {}".format(self.first_name, self.last_name)

    get_full_name.short_description = 'Name'

    def get_name(self):
        return self.get_full_name()

    get_name.short_description = 'Name'

    def get_short_name(self):
        """Returns the short name for the user."""
        return self.first_name

    get_short_name.short_description = 'Short name'

    def get_show_url(self):
        return reverse("users:detail", args=[self.username])

    def email_user(self, subject, message, from_email="colegend@colegend.org", **kwargs):
        """
        Sends an email to this User.
        """
        # TODO: Add link to website. (use Email template)
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def accept(self, accepter=None):
        self.is_accepted = True
        self.date_accepted = timezone.now()
        if not accepter:
            accepter = "CoLegend"
        message = "Congratulations - Your account has been verified by {}.\nwww.colegend.org".format(accepter)
        self.email_user("[CoLegend] Account verified!", message)
        self.save()

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
    message = render_to_string(
        "users/signup_manager_notification_email.txt",
        {'username': user, 'email': user.email})
    send_mail(
        subject="New user: {}".format(user),
        message=message,
        from_email="colegend@colegend.org",
        recipient_list=["connect@colegend.org"],
        fail_silently=True
    )
    # Notify the user.
    messages.add_message(request, messages.SUCCESS, 'We have received your application.')


class Contact(models.Model):
    owner = AutoOneToOneField(User)

    @property
    def first_name(self):
        return self.owner.first_name

    @first_name.setter
    def first_name(self, value):
        self.owner.first_name = value

    @property
    def last_name(self):
        return self.owner.last_name

    @last_name.setter
    def last_name(self, value):
        self.owner.last_name = value

    @property
    def email(self):
        return self.owner.email

    @email.setter
    def email(self, value):
        self.owner.email = value

    phone_number = PhoneField(help_text="Mobile or other phone number. Example: +4369910203039")

    street = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=5)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    GENDER_CHOICES = (
        ('M', 'Male Legend ♂'),
        ('F', 'Female Legend ♀'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    birthday = models.DateField()

    def __str__(self):
        return "{} ({})".format(self.get_name(), self.owner)

    def get_name(self):
        return self.owner.get_name()

    def get_gender_symbol(self):
        return self.get_gender_display()[-1:]

    def get_address(self):
        return "{}\n{} {}\n{}".format(
            self.street,
            self.postal_code, self.city,
            self.country
        )

    def get_age(self):
        born = self.birthday
        today = timezone.datetime.today()
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


class Profile(models.Model):
    """
    A user signup application model.
    This is used to get and save some information about the user upon account signup.
    """
    owner = AutoOneToOneField(User)

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
        return "{}'s Profile".format(self.owner)


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
    sound = models.BooleanField(verbose_name="Sound", default=True)
    keyboard = models.BooleanField(verbose_name="Keyboard Control", default=False)

    class Meta:
        verbose_name_plural = "Settings"

    def __str__(self):
        return "{}'s Settings".format(self.owner)
