from braces.views._access import AccessMixin
from django.contrib.auth.views import redirect_to_login
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from django.utils.safestring import mark_safe

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
            return redirect("users:inactive")
        return super(ActiveUserRequiredMixin, self).dispatch(
            request, *args, **kwargs)


class ManagerRequiredMixin(ActiveUserRequiredMixin):
    """
    View mixin that makes sure.. that only active managers get access.
    """
    def dispatch(self, request, *args, **kwargs):
        user = request.user
        if not (user.is_authenticated() and user.is_accepted and user.is_manager):
            raise PermissionDenied  # return a forbidden response
        return super(ManagerRequiredMixin, self).dispatch(
            request, *args, **kwargs)


class OwnedItemsMixin:
    def get_queryset(self):
        return super(OwnedItemsMixin, self).get_queryset().owned_by(self.request.user)


def get_icon(name):
    icon_map = {
        # views / models
        "journal": "book",
        "gathering": "comments-o",
        "challenge": "star",
        "dojo": "university",
        "vision": "eye",
        "agenda": "crosshairs",
        "project": "sitemap",
        "task": "check",
        "tag": "tag",
        "routine": "stack-overflow",
        "habit": "link",
        "legend": "paw",
        "quote": "quote-left",
        "contact": "envelope",
        "about": "info-circle",
        "feature": "road",
        "home": "home",
        "news": "newspaper-o",
        "tutorial": "graduation-cap",
        "profile": "user",
        "setting": "wrench",
        "usermanager": "user-md",
        "backend": "database",
        "test": "code",
        "search": "search",
        "info": "info",
        "avatar": "camera",
        "email": "at",
        "social-accounts": "cloud",
        "password": "lock",
        # controls
        "back": "arrow-left",
        "new": "plus",
        "edit": "pencil",
        "delete": "trash",
        "cancel": "times",
        "manage": "asterisk",
        "accept": "check-circle",
        # fields
        "location": "map-marker",
        "date": "calendar",
        "deadline": "calendar-o",
        "description": "file-text-o",
        # statuses
        "active": "dot-circle-o",
        "todo": "circle-o",
        "waiting": "clock-o",
        "done": "check-circle-o",
        "canceled": "times-circle-o",
        # other
        "sign-out": "sign-out",
        "signup": "sign-in",
    }
    if name in icon_map:
        name = icon_map.get(name)
    return mark_safe("""<i class="fa fa-{}"></i>""".format(name))
