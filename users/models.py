# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import
from django.conf import settings

from django.contrib.auth.models import AbstractUser, Group
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django_slack import slack_message


@python_2_unicode_compatible
class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(_("Name of User"), blank=True, max_length=255)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:profile', kwargs={'username': self.username})


@receiver(post_save, sender=User)
def new_user_manager_notification(sender, instance, created, **kwargs):
    if created:
        # manager_group, created_group = Group.objects.get_or_create(name="managers")
        # managers = [user.email for user in manager_group.user_set.all()]
        # TODO: Switch to managers group as soon as it is stable
        managers = ['connect@colegend.org']
        username = str(instance.username).title()
        subject = "{}New user: {}".format(settings.EMAIL_SUBJECT_PREFIX, username)
        message = "Hurray! {} has joined the circle of legends.".format(username)

        send_mail(subject, message, None, managers, fail_silently=False)

        slack_message('slack/message.slack', {'message': '@channel: {}'.format(message),})

# class Settings(models.Model):
#     owner = AutoOneToOneField(User, primary_key=True)
#     # ISO 639-1
#     ENGLISH = "EN"
#     LANGUAGE_CHOICES = (
#         (ENGLISH, 'English'),
#     )
#     language = models.CharField(max_length=2,
#                                 choices=LANGUAGE_CHOICES,
#                                 default=ENGLISH)
#     day_start = models.PositiveSmallIntegerField(
#         verbose_name="Day start time", default=0,
#         help_text="When does your day start? Enter number between 0 and 24 (24h clock).",
#         validators=[MaxValueValidator(24)])
#     sound = models.BooleanField(verbose_name="Sound", default=True)
#     keyboard = models.BooleanField(verbose_name="Keyboard Control", default=False)
#     background_color = RGBColorField(blank=True)
#
#     class Meta:
#         verbose_name_plural = "Settings"
#
#     def __str__(self):
#         return "{}'s Settings".format(self.owner)
