from django.contrib import messages
from django.contrib.auth.models import AbstractUser

__author__ = 'eraldo'


class User(AbstractUser):
    pass


from allauth.account.signals import user_signed_up
from django.dispatch import receiver

@receiver(user_signed_up, dispatch_uid="some.unique.string.id.for.allauth.user_signed_up")
def deactivate_user_after_signup(request, user, **kwargs):
    """
    Deactivate all new user accounts after signup.
    This is used to control the active users during alpha stage.

    :param request:
    :param user:
    :param kwargs:
    """
    # User signed up, now deactivate the account.
    user.is_active = False
    user.save()
    # Inform the user that he needs an admin to activate his account.
    message_deactivated = "Your account has been deactivated! - The project is still in a closed alpha state."
    messages.add_message(request, messages.INFO, message_deactivated)
