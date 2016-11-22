from django.template.defaultfilters import slugify

__author__ = 'Eraldo Energy'

fontawesome_icons = {
    # apps
    'mentor': 'compass',  # alt: 'check'
    'manager': 'briefcase',  # alt: 'check'
    # - status
    'open': 'square-o',
    'waiting': 'hourglass-half',
    'state-undefined': 'circle-thin',
    'closed': 'check-square-o',
    'done': 'check',
    'canceled': 'ban',
    #
    'date': 'calendar-o',
    'deadline': 'calendar-times-o',
    'estimate': 'clock-o',
    'inbox': 'inbox',
    #
    'journal': 'book',
    'story': 'magic',
    'vision': 'compass',
    'accademy': 'graduation-cap',
    'challenges': 'star',
    'game': 'game-pad',
    # community
    'community': 'group',
    'chat': 'commenting-o',
    'virtual-room': 'key',
    'guide': 'road',
    'gatherings': 'comments-o',
    'guidelines': 'map-signs',
    # project
    'process': 'refresh',
    'about': 'info-circle',
    'event': 'calendar-check-o',
    'events': 'calendar-check-o',
    'support': 'question-circle',
    'faq': 'question-circle-o',
    'personal-support': 'user-md',  # fa-life-ring
    'documentation': 'file-text-o',
    'tutorials': 'graduation-cap',
    'blog': 'newspaper-o',
    'styleguide': 'paint-brush',
    'quote': 'quote-left',
    # user
    'legend': 'user',
    'legends': 'group',
    'profile': 'user',
    'account': 'user',
    'settings': 'cogs',
    'join': 'user-plus',
    'login': 'sign-out',
    'log-in': 'sign-in',
    'logout': 'sign-out',
    #
    'address': 'map-marker',
    'occupation': 'briefcase',
    'phone': 'phone',
    'birthday': 'birthday-cake',
    'gender': 'transgender-alt',
    'name': 'user',
    'avatar': 'camera',
    # core
    'locked': 'lock',
    'tag': 'tag',
    'tags': 'tags',
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
    'more': 'ellipsis-v',
    #
    'scope': 'search-plus',
    'import': 'upload',
    #
    'actions': 'chevron-circle-down',
    #
    'content': 'align-left',
    'description': 'align-left',
    #
    'area-1': 'medkit',
    'area-2': 'smile-o',
    'area-3': 'sun-o',
    'area-4': 'heart',
    'area-5': 'microphone',
    'area-6': 'university',
    'area-7': 'moon-o',
    #
    'resources': 'file-text-o',
}

coicons = {
    'game': 'black-dice',
    'duo': 'dotted-duo',
    'tribe': 'dotted-square',
    'clan': 'dotted-circle',
    'apps': 'lego',
    'project': 'logo',
    'roles': 'wizard',
}


def get_icon_class(name):
    name = slugify(name)
    if name in coicons:
        return 'coicon co-{}'.format(coicons.get(name))
    else:
        name = fontawesome_icons.get(name, name)
        return 'fa fa-{}'.format(name)


icons = list(fontawesome_icons.keys()) + list(coicons.keys())
