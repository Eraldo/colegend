from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse, NoReverseMatch
from django.utils.html import format_html_join
from wagtail.wagtailadmin.menu import MenuItem
from wagtail.wagtailadmin.site_summary import SummaryItem
from wagtail.wagtailcore import hooks
from django.utils.translation import ugettext_lazy as _

from colegend.core.templatetags.core_tags import icon


@hooks.register('insert_global_admin_css')
def global_css():
    # Add extra CSS files to the admin like font-awesome
    css_files = [
        'components/fontawesome/css/font-awesome.min.css',
        'cms/css/wagtail-icons.css',
        'coicons/css/index.css',
    ]

    css_includes = format_html_join(
        '\n',
        '<link rel="stylesheet" href="{0}{1}">',
        ((settings.STATIC_URL, filename) for filename in css_files))

    return css_includes


class DjangoBackendLinkItem:
    @staticmethod
    def render(request):
        return '''<div class="wagtail-userbar__item ">
                    <div class="wagtail-action wagtail-icon wagtail-icon-pick">
                        <a href="{}" target="_parent">Backend</a>
                    </div>
                </div>'''.format(reverse('admin:index'))


@hooks.register('construct_wagtail_userbar')
def add_wagtail_icon_items(request, items):
    if request.user.is_superuser:
        items.append(DjangoBackendLinkItem())


class UsersSummaryItem(SummaryItem):
    template = 'cms/widgets/site_summary_item.html'
    order = 400

    def get_context(self):
        users = get_user_model().objects.all()
        return {
            'url': reverse('wagtailusers_users:index'),
            'icon': icon('legends', raw=True),
            'name': _('Legends'),
            'amount': users.count(),
        }


@hooks.register('construct_homepage_summary_items')
def add_users_summary_item(request, items):
    items.append(UsersSummaryItem(request))


class BackendMenuItem(MenuItem):
    def is_shown(self, request):
        return request.user.is_superuser


@hooks.register('register_admin_menu_item')
def register_backend_menu_item():
    return MenuItem(
        _('Backend'),
        reverse('admin:index'),
        classnames='icon icon-fa fa-database',
        order=10000
    )


@hooks.register('register_admin_menu_item')
def register_frontend_menu_item():
    url = '/'
    return MenuItem(
        _('Frontend'),
        url=url,
        classnames='icon icon-coicon co-logo',
        order=10000
    )
