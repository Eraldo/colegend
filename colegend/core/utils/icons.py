from enum import Enum

from django.template.defaultfilters import slugify

__author__ = 'Eraldo Energy'


class Icon(Enum):
    COLEGEND = 'co-colegend'  # 'infinite'
    PROFILE = 'finger-print'
    # apps
    HOME = 'home'
    ARCADE = 'game-controller-a'
    OFFICE = 'briefcase'
    COMMUNITY = 'bonfire'
    STUDIO = 'microphone'
    ACADEMY = 'co-academy'  # 'school'
    JOURNEY = 'co-journey'  # 'compass'
    # HOME
    DASHBOARD = 'navigate'
    HABITS = 'repeat'
    STATS = 'stats'
    TOOLS = 'hammer'
    # ARCADE
    ADVENTURES = 'pulse'
    GAMES = 'game-controller-b'
    CONTESTS = 'trophy'
    SHOP = 'cart'
    # OFFICE
    AGENDA = 'clipboard'
    OUTCOMES = 'checkbox-outline'
    ACHIEVEMENTS = 'medal'
    # COMMUNITY
    DUO = 'co-duo'  # 'person'
    CLAN = 'co-clan'  # 'contacts'
    TRIBE = 'co-tribe'  # 'people'
    MENTOR = 'co-wizard'  # 'man'
    # STUDIO
    JOURNAL = 'co-journal'  # 'book'
    INTERVIEW = 'text'
    STORY = 'co-story'  # 'brush'
    # ACADEMY
    BOOK_CLUB = 'co-book-club'  # 'bookmark'
    COURSES = 'ribbon'
    RESOURCES = 'co-resources'  # 'bookmarks'
    # JOURNEY
    QUESTS = 'co-quest'  # 'map'
    HERO = 'co-hero'  # 'happy'
    DEMON = 'co-demon'  # 'sad'
    QUOTE = 'quote'
    # life areas
    AREA1 = 'co-apple'  # 'nutrition'
    AREA2 = 'co-smiley'
    AREA3 = 'sunny'
    AREA4 = 'heart'
    AREA5 = 'megaphone'
    AREA6 = 'bulb'
    AREA7 = 'moon'
    # project
    NEWS = 'paper'
    EVENTS = 'calendar'
    SUPPORT = 'help-circle'
    SETTINGS = 'settings'
    BACKSTAGE = 'nuclear'
    FEEDBACK = 'paper-plane'
    # general
    SCOPE = 'aperture'
    SCHEDULE = 'time'
    DEADLINE = 'alarm'
    TAG = 'pricetag'
    TAGS = 'pricetags'
    CONTENT = 'text'
    STAR = 'star'
    STAR_EMPTY = 'star-outline'
    SELECT = 'checkmark'
    STREAK = 'flame'
    GEM = 'co-gem'
    PREMIUM = 'co-premium'
    BUY = 'cart'
    # UI
    MENU = 'menu'
    REFRESH = 'refresh'
    MORE = 'more'
    CREATE = 'add'
    EDIT = 'create'
    SAVE = 'checkmark'
    REMOVE = 'close-circle'
    DELETE = 'trash'
    CLOSE = 'close'
    CANCEL = 'close'
    SEARCH = 'search'
    EXPAND = 'expand'
    CONTRACT = 'contract'
    LOCKED = 'lock'
    LIKE = 'thumbs-up'
    DISLIKE = 'thumbs-down'
    ORDER = 'reorder'
    FILTER = 'funnel'
    # Media
    MUSIC = 'musical-note'
    PLAY = 'play'
    PAUSE = 'pause'
    MUTE = 'volume-off'
    STOP = 'square'
    UNMUTE = 'volume-up'
    # office
    STEPS = 'co-steps'  # 'checkbox-outline'
    STEP_OPEN = 'square-outline'
    STEP_CLOSED = 'checkbox'
    INBOX = 'filing'
    FOCUS = 'locate'
    MATCHING = 'git-compare'
    # statuses
    STATUS_FUTURE = 'cloud-circle'
    STATUS_WAITING = 'time'
    STATUS_CURRENT = 'checkmark-circle-outline'
    STATUS_DONE = 'checkmark-circle'
    STATUS_CANCELED = 'remove-circle'
    # community
    VIRTUAL_ROOM = 'videocam'

    @staticmethod
    def get_choices():
        return [(icon.value, icon.name.lower()) for icon in Icon]


# OLD

fontawesome_icons = {
    # apps
    'apps': 'cubes',
    'home': 'home',
    'arcade': 'gamepad',
    'office': 'briefcase',
    'community': 'group',
    'studio': 'microphone',
    'academy': 'graduation-cap',
    'journey': 'compass',
    #
    'news': 'newspaper-o',
    #
    'welcome': 'sign-in',
    'lab': 'flask',
    #
    'mentor': 'compass',
    'manager': 'briefcase',
    'balance': 'balance-scale',
    # 'games': 'trophy',
    # - status
    'state-undefined': 'circle-thin',
    'future': 'square',
    'waiting': 'hourglass-half',
    'current': 'square-o',
    'done': 'check',
    'canceled': 'ban',
    'closed': 'check-square-o',
    #
    'date': 'calendar-o',
    'deadline': 'calendar-times-o',
    'estimate': 'clock-o',
    'inbox': 'inbox',
    #
    'journal': 'book',
    'story': 'magic',
    'vision': 'compass',
    'academy': 'graduation-cap',
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
    'tutorial': 'graduation-cap',
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
    # 'area-1': 'apple', => see coicon
    # 'area-2': 'smile-o',
    'area-3': 'sun-o',
    'area-4': 'heart',
    'area-5': 'microphone',
    'area-6': 'university',
    'area-7': 'moon-o',
    #
    'resources': 'file-text-o',
}

coicons = {
    'area-1': 'apple',
    'area-2': 'smiley',
    'game': 'dice',
    'games': 'dice',
    'duo': 'dotted-duo',
    'clan': 'dotted-square',
    'tribe': 'dotted-square',
    # 'apps': 'lego',
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
