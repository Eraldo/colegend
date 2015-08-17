from collections import OrderedDict
from lib.views import get_icon

__author__ = 'eraldo'


class MenuItem:
    def __init__(self, name, url, arg=None, icon=None, keyboard_shortcut=None):
        self.name = name
        self.url = url
        self.arg = arg
        # add icon if given
        if icon:
            icon = get_icon(icon)
        self.icon = icon
        if keyboard_shortcut:
            self.keyboard_shortcut = keyboard_shortcut

    def __str__(self):
        return self.name


def menu(request):
    """A context processor that provides menu_items."""
    user = request.user
    menu_items = OrderedDict()
    menu_items['mentor'] = [
        MenuItem("Journal", url="journals:index", icon="journal", keyboard_shortcut='g j'),
        MenuItem("Gatherings", url="gatherings:home", icon="gathering", keyboard_shortcut='g g'),
        MenuItem("Challenges", url="challenges:challenge_list", icon="challenge", keyboard_shortcut='g c'),
        MenuItem("Dojo", url="dojo:home", icon="dojo", keyboard_shortcut='g d'),
        MenuItem("Life Vision", url="visions:vision_list", icon="vision", keyboard_shortcut='g v'),
    ]
    if user.is_authenticated() and user.is_tester:
        menu_items['mentor_extra'] = [
        ]
    menu_items['manager'] = [
        MenuItem("Agenda", url="manager:agenda", icon="agenda", keyboard_shortcut='g a'),
        MenuItem("Projects", url="projects:project_list", icon="project", keyboard_shortcut='g p'),
        MenuItem("Tasks", url="tasks:task_list", icon="task", keyboard_shortcut='g t'),
        MenuItem("Tags", url="tags:tag_list", icon="tag", keyboard_shortcut='g x'),
        MenuItem("Trackers", url="trackers:tracker_list", icon="tracker", keyboard_shortcut='g r'),
    ]
    if user.is_authenticated() and user.is_tester:
        menu_items['manager_extra'] = [
            MenuItem("Routines", url="routines:routine_list", icon="routine"),
            MenuItem("Habits", url="habits:habit_list", icon="habit"),
        ]
    menu_items['motivator'] = [
        MenuItem("Legend", url="legend:home", icon="legend", keyboard_shortcut='g l'),
        MenuItem("Quotes", url="quotes:quote_list", icon="quote", keyboard_shortcut='g q'),
        MenuItem("Stats", url="stats:home", icon="stats", keyboard_shortcut='g S'),
        MenuItem("Cards", url="cards:picker", icon="card", keyboard_shortcut='g C'),
    ]
    if user.is_authenticated() and user.is_tester:
        menu_items['motivator_extra'] = [
        ]
    menu_items['operator'] = [
        MenuItem("Contact", url="contact", icon="contact", keyboard_shortcut='g m'),
        MenuItem("About", url="about", icon="about"),
        MenuItem("News", url="news:newsblock_list", icon="news", keyboard_shortcut='g n'),
        MenuItem("Tutorials", url="tutorials:tutorial_list", icon="tutorial", keyboard_shortcut='g ?'),
        MenuItem("Search", url="search", icon="search", keyboard_shortcut='g s'),
        MenuItem("Home", url="home", icon="home", keyboard_shortcut='g h'),
        MenuItem("Features", url="features:feature_list", icon="feature"),
    ]
    if user.is_authenticated() and user.is_tester:
        menu_items['operator_extra'] = [
        ]
    menu_items['account'] = [
        MenuItem("Profile", url="users:detail", arg=request.user, icon="profile", keyboard_shortcut='g u'),
        MenuItem("Settings", url="users:settings", icon="setting", keyboard_shortcut='g *'),
    ]
    if user.is_authenticated() and user.is_manager:
        menu_items['manage'] = [
            MenuItem("Users", url="users:manage", icon="usermanager"),
        ]
    if user.is_authenticated() and user.is_superuser:
        menu_items['admin'] = [
            MenuItem("Backend", url="admin:index", icon="backend", keyboard_shortcut='g %'),
            MenuItem("Test", url="test", icon="test"),
        ]
    return {'menu_items': menu_items}
