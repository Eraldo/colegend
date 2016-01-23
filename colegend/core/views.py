from django.contrib import messages
from django.shortcuts import redirect
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _


class CheckpointsRequiredMixin(object):
    """
    A django View mixin that checks if the user has got the checkpoints which are specified as an attribute of the class.
    :required_checkpoints: An iterable of strings with checkpoint names.
    """
    required_checkpoints = None

    def has_checkpoints(self):
        """
        Checks if the user has a the checkpoints as specified by the `required_checkpoints` class attribute.
        :return: `True` if check passes; `False` if the user did not pass all requirements.
        """
        user = self.request.user
        checkpoints = self.required_checkpoints
        if not checkpoints:
            raise NotImplementedError(
                _('{0} is missing the "required_checkpoints" attribute.').format(self.__class__.__name__)
            )
        for checkpoint in checkpoints:
            check = user.has_checkpoint(checkpoint)
            if not check:
                return False
        return True

    def handle_insufficient_checkpoints(self):
        """
        Rediredt the user to the page he came from and
        show a message pointing him to the game to unlock more features.
        :return: The page the user came from or his home.
        """
        request = self.request
        user = request.user
        game_url = user.game.get_absolute_url()
        game_link = '<a href="{}">game</a>'.format(game_url)
        message = _('You need to unlock this feature in the {}.').format(game_link)
        messages.warning(request, mark_safe(message))
        return redirect(request.META.get('HTTP_REFERER', '/'))

    def dispatch(self, request, *args, **kwargs):
        has_checkpoints = self.has_checkpoints()
        if not has_checkpoints:
            return self.handle_insufficient_checkpoints()
        return super().dispatch(request, *args, **kwargs)


class RolesRequiredMixin(object):
    """
    A django View mixin that checks if the user has got the roles which are specified as an attribute of the class.
    :required_roles: An iterable of strings with role names.
    """
    required_roles = None

    def has_roles(self):
        """
        Checks if the user has a the roles as specified by the `required_roles` class attribute.
        :return: `True` if check passes; `False` if the user did not pass all requirements.
        """
        user = self.request.user
        roles = self.required_roles
        if not roles:
            raise NotImplementedError(
                _('{0} is missing the "required_roles" attribute.').format(self.__class__.__name__)
            )
        for role in roles:
            check = user.has_role(role)
            if not check:
                return False
        return True

    def handle_insufficient_roles(self):
        """
        Rediredt the user to the page he came from and
        show a message pointing him to the game to unlock more features.
        :return: The page the user came from or his home.
        """
        request = self.request
        message = _('You currently do not have the required roles.')
        messages.warning(request, message)
        return redirect(request.META.get('HTTP_REFERER', '/'))

    def dispatch(self, request, *args, **kwargs):
        has_roles = self.has_roles()
        if not has_roles:
            return self.handle_insufficient_roles()
        return super().dispatch(request, *args, **kwargs)
