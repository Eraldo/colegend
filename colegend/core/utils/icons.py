__author__ = 'Eraldo Energy'

fontawesome_icons = {
    # apps
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
    'event': 'calendar-check-o',
    'guide': 'road',
    'gatherings': 'comments-o',
    # project
    'about': 'info-circle',
    'support': 'question-circle',
    'documentation': 'file-text-o',
    'news': 'newspaper-o',
    'styleguide': 'paint-brush',
    'quote': 'quote-left',
    # user
    'legend': 'user',
    'legends': 'group',
    'profile': 'user',
    'settings': 'cogs',
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
    if name in coicons:
        return 'coicon co-{}'.format(coicons.get(name))
    else:
        name = fontawesome_icons.get(name, name)
        return 'fa-{}'.format(name)


icons = list(fontawesome_icons.keys()) + list(coicons.keys())
