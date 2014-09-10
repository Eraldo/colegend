from django.contrib import messages
from django.contrib.auth.models import AbstractUser
from django.core.mail import mail_admins

__author__ = 'eraldo'


class User(AbstractUser):
    pass

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
