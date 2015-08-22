from braces.views._access import AccessMixin
from django.contrib.auth.views import redirect_to_login
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from django.conf import settings

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
            return redirect('users:inactive')
        return super().dispatch(
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


class AdminRequiredMixin(ActiveUserRequiredMixin):
    """
    View mixin that makes sure.. that only superusers (admins) get access.
    """
    def dispatch(self, request, *args, **kwargs):
        user = request.user
        if not user.is_superuser:
            raise PermissionDenied  # return a forbidden response
        return super().dispatch(
            request, *args, **kwargs)


class OwnedItemsMixin:
    def get_queryset(self):
        return super(OwnedItemsMixin, self).get_queryset().owned_by(self.request.user)


def get_icon(name, raw=False):
    icon_map = {
        # mentor
        'journal': 'book',
        'gathering': 'comments-o',
        'chat': 'wechat',
        'virtual-room': 'cube',  # Alternative icons: group cube video-camera
        'challenge': 'star',
        'dojo': 'university',
        'vision': 'eye',
        # manager
        'agenda': 'crosshairs',
        'project': 'sitemap',
        'task': 'check',
        'tag': 'tag',
        'routine': 'stack-overflow',
        'habit': 'link',
        'tracker': 'line-chart',
        'chart': 'bar-chart',
        # motivator
        'map': 'map',
        'legend': 'paw',
        'quote': 'quote-left',
        'stats': 'dashboard',
        'card': 'image',
        # operator
        'contact': 'envelope',
        'about': 'info-circle',
        'feature': 'road',
        'home': 'home',
        'news': 'newspaper-o',
        'tutorial': 'question-circle',
        'profile': 'user',
        'setting': 'wrench',
        'usermanager': 'user-md',
        'backend': 'database',
        'test': 'code',
        'search': 'search',
        'info': 'info',
        'avatar': 'camera',
        'email': 'at',
        'social-accounts': 'cloud',
        'password': 'lock',
        'sign-out': 'sign-out',
        'signup': 'sign-in',
        # notifications
        'notification-unread': 'bell',
        'notification': 'bell-o',
        'mark_read': 'bell-slash',
        # controls
        'back': 'arrow-left',
        'new': 'plus',
        'edit': 'pencil',
        'delete': 'trash',
        'cancel': 'times',
        'remove': 'remove',
        'manage': 'asterisk',
        'accept': 'check-circle',
        # fields
        'location': 'map-marker',
        'date': 'calendar',
        'deadline': 'calendar-o',
        'time-estimate': 'clock-o',
        'description': 'file-text-o',
        # statuses
        'next': 'dot-circle-o',
        'todo': 'circle-o',
        'waiting': 'clock-o',
        'someday': 'circle-o-notch',
        'maybe': 'circle-thin',
        'done': 'check-circle-o',
        'canceled': 'times-circle-o',
        # categories
        'category-7': 'moon-o',
        'category-6': 'graduation-cap',  # alternatives: lightbulb-o',
        'category-5': 'child',
        'category-4': 'leaf',
        'category-3': 'credit-card',
        'category-2': 'film',  # alternatives: gamepad
        'category-1': 'heart-o',  # alternatives: cutlery
        # other
        'streak': 'link',
        'share': 'share',
        'prompt': 'chevron-right',
        'quick-command': 'asterisk',
        'locked': 'lock',
        # trackers
        'rating': 'star',
        'number': 'slack',
        'sleep': 'bed',
        'weight': 'dashboard',
        'sex': 'user-times',
        'transaction': 'money',
        'walk': 'tree',
        'joke': 'smile-o',
        'dream': 'picture-o',
    }
    if name in icon_map:
        name = icon_map.get(name)
    if raw:
        return name
    return mark_safe("""<i class='fa fa-{}'></i>""".format(name))


def get_sound(name):
    sound_map = {
        'task-success': 'task-success.wav',
        'project-success': 'project-success.mp3',
    }
    if name in sound_map:
        context = {'sound': name, 'STATIC_URL': settings.STATIC_URL, 'file': sound_map[name]}
        return render_to_string('lib/_audio.html', dictionary=context)

