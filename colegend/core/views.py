from django.contrib import messages
from django.shortcuts import redirect
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _
from django.views.generic import CreateView, UpdateView


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

    def handle_insufficient_checkpoints(self, request, *args, **kwargs):
        """
        Rediredt the user to the page he came from and
        show a message pointing him to the game to unlock more features.
        :return: The page the user came from or his home.
        """
        user = request.user
        if user.is_superuser:
            message = _('Viewing as {}.'.format('admin'))
            messages.info(request, message)
            return super().dispatch(request, *args, **kwargs)
        else:
            game_url = user.game.get_absolute_url()
            game_link = '<a href="{}">game</a>'.format(game_url)
            message = _('You need to unlock this feature in the {}.').format(game_link)
            messages.warning(request, mark_safe(message))
            return redirect(request.META.get('HTTP_REFERER', '/'))

    def dispatch(self, request, *args, **kwargs):
        has_checkpoints = self.has_checkpoints()
        if not has_checkpoints:
            return self.handle_insufficient_checkpoints(request, *args, **kwargs)
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

    def handle_insufficient_roles(self, request, *args, **kwargs):
        """
        Rediredt the user to the page he came from and
        show a message pointing him to the game to unlock more features.
        :return: The page the user came from or his home.
        """
        user = request.user
        if user.is_superuser:
            message = _('Viewing as {}.'.format('admin'))
            messages.info(request, message)
            return super().dispatch(request, *args, **kwargs)
        else:
            message = _('You currently do not have the required roles.')
            messages.warning(request, message)
            return redirect(request.META.get('HTTP_REFERER', '/'))

    def dispatch(self, request, *args, **kwargs):
        has_roles = self.has_roles()
        if not has_roles:
            return self.handle_insufficient_roles(request, *args, **kwargs)
        return super().dispatch(request, *args, **kwargs)


class OwnerRequiredMixin(object):
    """
    A django View mixin that checks if the user has got ownership of the resource.
    """

    def has_ownership(self):
        """
        Checks if the user is the owner of the resource.
        :return: `True` if check passes; `False` if the user did not pass all requirements.
        """
        user = self.request.user
        object = self.get_object()
        if object.owned_by(user):
            return True
        else:
            return False

    def handle_no_ownership(self, request, *args, **kwargs):
        """
        Rediredt the user to the page he came from and
        show a message informing him of the lack of ownership.
        :return: The page the user came from or his home.
        """
        user = request.user
        if user.is_superuser:
            message = _('Viewing as {}.'.format('admin'))
            messages.info(request, message)
            return super().dispatch(request, *args, **kwargs)
        else:
            message = _('Ownership required.')
            messages.warning(request, message)
            return redirect(request.META.get('HTTP_REFERER', '/'))

    def dispatch(self, request, *args, **kwargs):
        ownership = self.has_ownership()
        if not ownership:
            return self.handle_no_ownership(request, *args, **kwargs)
        return super().dispatch(request, *args, **kwargs)


class OwnedCreateView(CreateView):
    """
    Adds the owner to the form and sets the current user as the default owner.
    """

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['owner'] = self.request.user
        return kwargs

    def get_initial(self):
        initial = super().get_initial()
        initial['owner'] = self.request.user
        return initial


class OwnedUpdateView(UpdateView):
    """
    Adds the owner to the form.
    """

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['owner'] = self.request.user
        return kwargs


class OwnedItemsMixin(object):
    """
    Only uses owned items as the the default queryset.
    """

    def get_queryset(self):
        user = self.request.user
        return super().get_queryset().owned_by(user)
