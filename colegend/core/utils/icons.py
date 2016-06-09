from django.template.loader import render_to_string

__author__ = 'Eraldo Energy'

icon_dict = {
    # conscious
    'conscious': 'graduation-cap',
    'journal': 'book',
    # connected
    'connected': 'heart',
    'legend': 'user',
    'legends': 'user',
    # continuous
    'continuous': 'paw',
    # orga
    'settings': 'wrench',
    'sign-out': 'sign-out',
    'locked': 'lock',
    #
    'gatherings': 'comments-o',
    'challenges': 'star',
    'journal': 'book',
    'manager': 'check',
    #
    'tag': 'tag',
    #
    'create': 'plus',
    'detail': 'eye',
    'update': 'pencil',
    'delete': 'trash',
    #
    'checked': 'check-square-o',
    'unchecked': 'square-o',
    #
    'previous': 'chevron-left',
    'next': 'chevron-right',
    #
    'scope': 'search-plus',
    'import': 'upload',
    #
    'actions': 'chevron-circle-down',
    #
    'event': 'calendar',
    'feature': 'road',
    'news': 'newspaper-o',
    'quote': 'quote-left',
    'role': 'user-md',
    'story': 'magic',
    'tool': 'gavel',
    #
    'date': 'calendar',
    'deadline': 'calendar-o',
    'content': 'align-left',
    #
    'address': 'map-marker',
    'occupation': 'briefcase',
    'phone': 'phone',
    'birthday': 'birthday-cake',
    'gender': 'transgender-alt',
    'name': 'user',
    'avatar': 'camera',
    #
    'support': 'question-circle',
    'faq': 'question',
    'documentation': 'file-text-o',
    #
    'game': 'trophy',
    # core
    'more': 'ellipsis-v',
    # manager
    'description': 'align-left',
    'estimate': 'clock-o',
    # status
    'open': 'square-o',
    'waiting': 'hourglass-half',
    'closed': 'check-square-o',
}


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
