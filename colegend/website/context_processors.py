from collections import OrderedDict
from random import randint
from lib.views import get_icon
from quotes.models import Quote

__author__ = 'eraldo'


class MenuItem:
    def __init__(self, name, url, arg=None, icon=None, keyboard_shortcut=None, category=None):
        self.name = name
        self.url = url
        self.arg = arg
        # add icon if given
        if icon:
            icon = get_icon(icon, raw=True)
        self.icon = icon
        if keyboard_shortcut:
            self.keyboard_shortcut = keyboard_shortcut
        if category:
            self.category = category

    def __str__(self):
        return self.name


def menu(request):
    """A context processor that provides menu_items."""
    user = request.user
    menu_items = OrderedDict()
    menu_items[7] = [
        MenuItem("About", url="about", icon="about", category=7),
        MenuItem("Life Vision", url="visions:vision_list", icon="vision", keyboard_shortcut='g v', category=7),
    ]
    menu_items[6] = [
        MenuItem("Dojo", url="dojo:home", icon="dojo", keyboard_shortcut='g d', category=6),
        MenuItem("Stats", url="stats:home", icon="stats", keyboard_shortcut='g S', category=6),
        MenuItem("Search", url="search", icon="search", keyboard_shortcut='g s', category=6),
        MenuItem("Features", url="features:feature_list", icon="feature", category=6),
    ]
    menu_items[5] = [
        MenuItem("Contact", url="contact", icon="contact", keyboard_shortcut='g m', category=5),
        MenuItem("News", url="news:newsblock_list", icon="news", keyboard_shortcut='g n', category=5),
        MenuItem("Gatherings", url="gatherings:home", icon="gathering", keyboard_shortcut='g g', category=5),
    ]
    menu_items[4] = [
        MenuItem("Home", url="home", icon="home", keyboard_shortcut='g h', category=4),
        MenuItem("Profile", url="users:detail", arg=request.user, icon="profile", keyboard_shortcut='g u', category=4),
        MenuItem("Legend", url="legend:home", icon="legend", keyboard_shortcut='g l', category=4),
        MenuItem("Tags", url="tags:tag_list", icon="tag", keyboard_shortcut='g x', category=4),
    ]
    menu_items[3] = [
        MenuItem("Journal", url="journals:index", icon="journal", keyboard_shortcut='g j', category=3),
        MenuItem("Agenda", url="manager:agenda", icon="agenda", keyboard_shortcut='g a', category=3),
        MenuItem("Projects", url="projects:project_list", icon="project", keyboard_shortcut='g p', category=3),
        MenuItem("Tasks", url="tasks:task_list", icon="task", keyboard_shortcut='g t', category=3),
    ]
    menu_items[2] = [
        MenuItem("Challenges", url="challenges:challenge_list", icon="challenge", keyboard_shortcut='g c', category=2),
        MenuItem("Quotes", url="quotes:quote_list", icon="quote", keyboard_shortcut='g q', category=2),
        MenuItem("Cards", url="cards:picker", icon="card", keyboard_shortcut='g C', category=2),
    ]
    menu_items[1] = [
        MenuItem("Trackers", url="trackers:tracker_list", icon="tracker", keyboard_shortcut='g r', category=1),
        MenuItem("Tutorials", url="tutorials:tutorial_list", icon="tutorial", keyboard_shortcut='g ?', category=1),
        MenuItem("Settings", url="users:settings", icon="setting", keyboard_shortcut='g *', category=1),
    ]
    if user.is_authenticated() and user.is_manager:
        menu_items[1] += [
            MenuItem("Users", url="users:manage", icon="usermanager", category=1),
        ]
    if user.is_authenticated() and user.is_superuser:
        menu_items[1] += [
            MenuItem("Backend", url="admin:index", icon="backend", keyboard_shortcut='g %', category=1),
            MenuItem("Test", url="test", icon="test", category=1),
        ]
    return {'menu_items': menu_items}


def menu_feed(request):
    if randint(0, 1) or not request.user.is_authenticated():
        quote = Quote.objects.daily_quote()
        return {'daily_quote_feed': quote}
    elif request.user.is_authenticated():
        topic_of_the_year = request.user.journal.topic_of_the_year
        return {'topic_of_the_year_feed': topic_of_the_year}
