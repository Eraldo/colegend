from bootstrap3.components import render_icon
from django.utils.safestring import mark_safe

__author__ = 'eraldo'


class MenuItem:
    positions = ["main", "extra", "settings"]

    def __init__(self, name, url, icon=None):
        self.name = name
        self.url = url
        # add icon if given
        if icon:
            icon = mark_safe(render_icon(icon))
        self.icon = icon

    def __str__(self):
        return self.name


def menu(request):
    """A context processor that provides menu_items."""
    menu_items = {
        'main': [
            MenuItem("Projects", url="projects:project_list", icon="folder-open"),
            MenuItem("Tasks", url="tasks:task_list", icon="check"),
            MenuItem("Tags", url="tags:tag_list", icon="tags"),
        ],
        'extra': [
            MenuItem("Home", url="home", icon="home"),
            MenuItem("About", url="about", icon="info-sign"),
            MenuItem("Meetings", url="meetings", icon="map-marker"),
            MenuItem("vision", url="visions:vision_list", icon="eye-open"),
            MenuItem("Feature Roadmap", url="features:feature_list", icon="road"),
        ],
        'settings': [
            MenuItem("settings", url="home", icon="wrench"),
            MenuItem("contact", url="home", icon="envelope"),
        ],
        'experimental': [
            MenuItem("routines", url="routines:routine_list", icon="asterisk"),
            MenuItem("habits", url="habits:habit_list", icon="link"),
            MenuItem("commands", url="commands", icon="bullhorn"),
        ],
        'admin': [
            MenuItem("test", url="test", icon="eye-open"),
        ],
    }
    return {'menu_items': menu_items}
