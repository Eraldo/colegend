# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from allauth.account.signals import user_signed_up
from django.conf import settings

from django.contrib.auth.models import AbstractUser, Group
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.db import models
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
        return reverse('legends:profile', kwargs={'username': self.username})

    class Meta:
        verbose_name = "Legend"
        verbose_name_plural = "Legends"


@receiver(user_signed_up)
def new_user_manager_notification(request, user, **kwargs):
    """
    Sends an email notification and a slack message upon successful user signup.
    The Email is sent to the site managers.
    The slack message is sent to the default slack channel from the project settings.
    :param request:
    :param user:
    :param kwargs:
    :return:
    """
    # manager_group, created_group = Group.objects.get_or_create(name="managers")
    # managers = [user.email for user in manager_group.user_set.all()]
    # TODO: Switch to managers group as soon as it is stable
    managers = ['connect@colegend.org']
    username = str(user.username)
    subject = "{}New user: {}".format(settings.EMAIL_SUBJECT_PREFIX, username)
    message = "Hurray! {} has joined the circle of legends.".format(username)

    send_mail(subject, message, None, managers, fail_silently=False)
    # TODO: Fix backend isse: https://app.getsentry.com/eraldo/colegend-staging/issues/102969964/
    # Then remove fail_silently
    slack_message('slack/message.slack', {'message': '@channel: {}'.format(message), }, fail_silently=True)
