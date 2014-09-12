from django.contrib import messages
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import mail_admins
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


class User(AbstractUser):
    contact = models.OneToOneField(Contact, null=True)
    profile = models.OneToOneField(Profile, null=True)
    # Roles
    is_tester = models.BooleanField(verbose_name="tester status", default=False,
                                    help_text="Designates whether the user can access the site's test features.")

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


@receiver(user_signed_up, dispatch_uid="some.unique.string.id.for.allauth.user_signed_up")
def notify_admin_after_signup(request, user, **kwargs):
    """
    Inform the admin that a new user has signed up for the system.
    This is used to control the active users during alpha stage.

    :param request:
    :param user:
    :param kwargs:
    """

    # Notify the admins.
    mail_admins(
        subject="New user: {}".format(user),
        message="A new user has signed up:\nUsername: {}\nEmail: {}".format(user, user.email),
        fail_silently=True
    )
    # Deactivate the account.
    user.is_active = False
    user.save()
    # Inform the user that he needs an admin to activate his account.
    message_deactivated = "Your account has been deactivated! - The project is still in a closed alpha state."
    messages.add_message(request, messages.INFO, message_deactivated)
