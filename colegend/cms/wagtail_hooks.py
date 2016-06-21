from django.conf import settings
from django.utils.html import format_html_join
from wagtail.wagtailadmin.menu import MenuItem
from wagtail.wagtailcore import hooks


@hooks.register('insert_global_admin_css')
def global_css():
    # Add extra CSS files to the admin like font-awesome
    css_files = [
        'components/fontawesome/css/font-awesome.min.css',
        'cms/css/wagtail-icons.css',
        'fonts/coicons/style.css',
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
                </div>'''.format(settings.ADMIN_URL)


@hooks.register('construct_wagtail_userbar')
def add_wagtail_icon_items(request, items):
    if request.user.is_superuser:
        items.append(DjangoBackendLinkItem())


class DjangoAdminMenuItem:
    order = 90000

    @staticmethod
    def render_html(request):
        output = '''<li class="menu-item">
                        <a href="/admin/" class="fa fa-database">Admin</a>
                    </li>'''
        return output


@hooks.register('construct_main_menu')
def main_menu_django_admin_item(request, menu_items):
    if request.user.is_superuser:
        menu_items.append(DjangoAdminMenuItem())

# Does not seem to work yet!?
# @hooks.register('register_admin_menu_item')
# def register_admin_menu_item():
#     return MenuItem('Backend', '#', classnames='icon icon-folder-inverse', order=10000)
