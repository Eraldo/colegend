from braces.views._access import AccessMixin
from django.contrib.auth.views import redirect_to_login
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect

__author__ = 'eraldo'


class ActiveUserRequiredMixin(AccessMixin):
    """
    View mixin which verifies that the user is authenticated and has been accepted.

    NOTE:
        This should be the left-most mixin of a view, except when
        combined with CsrfExemptMixin - which in that case should
        be the left-most mixin.
    """
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            if self.raise_exception:
                raise PermissionDenied  # return a forbidden response
            else:
                return redirect_to_login(request.get_full_path(),
                                         self.get_login_url(),
                                         self.get_redirect_field_name())

        if not request.user.is_accepted:
            return redirect("inactive")
        return super(ActiveUserRequiredMixin, self).dispatch(
            request, *args, **kwargs)


class OwnedItemsMixin:
    def get_queryset(self):
        return super(OwnedItemsMixin, self).get_queryset().owned_by(self.request.user)
