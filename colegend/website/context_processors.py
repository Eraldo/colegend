from django.utils.safestring import mark_safe
from lib.views import get_icon

__author__ = 'eraldo'


class MenuItem:

    def __init__(self, name, url, arg=None, icon=None):
        self.name = name
        self.url = url
        self.arg = arg
        # add icon if given
        if icon:
            icon = get_icon(icon)
        self.icon = icon

    def __str__(self):
        return self.name


def menu(request):
    """A context processor that provides menu_items."""
    menu_items = {
        'mentor': [
            MenuItem("Journal", url="journals:dayentry_list", icon="journal"),
            MenuItem("Gatherings", url="gatherings:home", icon="gathering"),
            MenuItem("Challenges", url="challenges:challenge_list", icon="challenge"),
            MenuItem("Dojo", url="dojo:home", icon="dojo"),
            MenuItem("Life Vision", url="visions:vision_list", icon="vision"),
        ],
        'mentor_extra': [
        ],
        'manager': [
            MenuItem("Agenda", url="manager:agenda", icon="agenda"),
            MenuItem("Projects", url="projects:project_list", icon="project"),
            MenuItem("Tasks", url="tasks:task_list", icon="task"),
            MenuItem("Tags", url="tags:tag_list", icon="tag"),
        ],
        'manager_extra': [
            MenuItem("Routines", url="routines:routine_list", icon="routine"),
            MenuItem("Habits", url="habits:habit_list", icon="habit"),
        ],
        'motivator': [
            MenuItem("Legend", url="legend:home", icon="legend"),
            MenuItem("Quotes", url="quotes:quote_list", icon="quote"),
        ],
        'motivator_extra': [
        ],
        'operator': [
            MenuItem("Contact", url="contact", icon="contact"),
            MenuItem("About", url="about", icon="about"),
            MenuItem("Features", url="features:feature_list", icon="feature"),
            MenuItem("Home", url="home", icon="home"),
            MenuItem("News", url="news:newsblock_list", icon="news"),
            MenuItem("Tutorials", url="tutorials:tutorial_list", icon="tutorial"),
        ],
        'operator_extra': [
        ],
        'account': [
            MenuItem("Profile", url="users:detail", arg=request.user, icon="profile"),
            MenuItem("Settings", url="users:settings", icon="setting"),
        ],
        'manage': [
            MenuItem("Users", url="users:manage", icon="usermanager"),
        ],
        'admin': [
            MenuItem("Backend", url="admin:index", icon="backend"),
            MenuItem("Test", url="test", icon="test"),
        ],
    }
    return {'menu_items': menu_items}
