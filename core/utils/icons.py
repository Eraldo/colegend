from django.template.loader import render_to_string

__author__ = 'Eraldo Energy'

icon_dict = {
    # conscious
    'conscious': 'graduation-cap',
    # connected
    'connected': 'heart',
    'legend': 'user',
    # continuous
    'continuous': 'paw',
    # orga
    'settings': 'wrench',
    'sign-out': 'sign-out',
    'locked': 'lock',

    'gatherings': 'comments-o',
    'challenges': 'star',
    'journal': 'book',
    'manager': 'check',

    'checked': 'check-square-o',
    'unchecked': 'square-o',

    'event': 'calendar',
    'feature': 'road',
    'news': 'newspaper-o',
    'quote': 'quote-left',
    'role': 'user-md',
    'story': 'magic',
    'tool': 'gavel',

    'address': 'map-marker',
    'occupation': 'briefcase',
    'phone': 'phone-square',
    'birthday': 'birthday-cake',
    'gender': 'transgender-alt',
    'name': 'user',
    'avatar': 'camera',

    'support': 'question-circle',
    'faq': 'question',
    'documentation': 'file-text-o',
}


# OLD
#
# # mentor
# 'journal': 'book',
# 'gathering': 'comments-o',
# 'chat': 'wechat',
# 'virtual-room': 'cube',  # Alternative icons: group cube video-camera
# 'challenge': 'star',
# 'dojo': 'university',
# 'vision': 'eye',
# # manager
# 'agenda': 'crosshairs',
# 'project': 'sitemap',
# 'task': 'check',
# 'tag': 'tag',
# 'routine': 'stack-overflow',
# 'habit': 'link',
# 'tracker': 'line-chart',
# 'chart': 'bar-chart',
# # motivator
# 'map': 'map',
# 'quote': 'quote-left',
# 'stats': 'dashboard',
# 'card': 'image',
# # operator
# 'contact': 'envelope',
# 'about': 'info-circle',
# 'feature': 'road',
# 'home': 'home',
# 'news': 'newspaper-o',
# 'tutorial': 'question-circle',
# 'profile': 'user',
# 'usermanager': 'user-md',
# 'backend': 'database',
# 'test': 'code',
# 'search': 'search',
# 'info': 'info',
# 'avatar': 'camera',
# 'email': 'at',
# 'social-accounts': 'cloud',
# 'password': 'lock',
# 'sign-out': 'sign-out',
# 'signup': 'sign-in',
# # notifications
# 'notification-unread': 'bell',
# 'notification': 'bell-o',
# 'mark_read': 'bell-slash',
# # controls
# 'back': 'arrow-left',
# 'new': 'plus',
# 'edit': 'pencil',
# 'delete': 'trash',
# 'cancel': 'times',
# 'remove': 'remove',
# 'manage': 'asterisk',
# 'accept': 'check-circle',
# # fields
# 'location': 'map-marker',
# 'date': 'calendar',
# 'deadline': 'calendar-o',
# 'time-estimate': 'clock-o',
# 'description': 'file-text-o',
# # statuses
# 'next': 'dot-circle-o',
# 'todo': 'circle-o',
# 'waiting': 'clock-o',
# 'someday': 'circle-o-notch',
# 'maybe': 'circle-thin',
# 'done': 'check-circle-o',
# 'canceled': 'times-circle-o',
# # categories
# 'category-7': 'moon-o',
# 'category-6': 'graduation-cap',  # alternatives: lightbulb-o',
# 'category-5': 'child',
# 'category-4': 'leaf',
# 'category-3': 'credit-card',
# 'category-2': 'film',  # alternatives: gamepad
# 'category-1': 'heart-o',  # alternatives: cutlery
# # other
# 'streak': 'link',
# 'share': 'share',
# 'prompt': 'chevron-right',
# 'quick-command': 'asterisk',
# 'locked': 'lock',
# 'import': 'level-down',
# 'export': 'level-up',
# # trackers
# 'rating': 'star',
# 'number': 'slack',
# 'sleep': 'bed',
# 'weight': 'dashboard',
# 'sex': 'user-times',
# 'transaction': 'money',
# 'walk': 'tree',
# 'joke': 'smile-o',
# 'dream': 'picture-o',


def get_icon_name(name):
    return icon_dict.get(name, name)


def get_icon(name, large=False, fixed=False, spin=False, pulse=False, li=False, rotate=False, border=False, color=False,
             classes=None, raw=False):
    name = get_icon_name(name)
    if raw:
        return name
    context = {
        'prefix': 'fa',
        'name': name,
        'large': large,
        'fixed': fixed,
        'spin': spin,
        'pulse': pulse,
        'li': li,
        'rotate': rotate,
        'border': border,
        'color': color,
        'classes': classes,
    }
    return render_to_string('widgets/icon.html', context=context)
