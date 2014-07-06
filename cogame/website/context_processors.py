from bootstrap3.components import render_icon
from django.utils.safestring import mark_safe

__author__ = 'eraldo'


class MenuItem:
    positions = ["main", "extra", "settings"]

    def __init__(self, name, url, icon=None, position=None):
        self.name = name
        self.url = url
        # add icon if given
        if icon:
            icon = mark_safe(render_icon(icon))
        self.icon = icon
        # add position if given
        if position and position in self.positions:
            self.position = position
        else:
            self.position = "main"

    def __str__(self):
        return self.name


def menu(request):
    """A context processor that provides menu_items."""
    menu_items = {
        'main': [
            MenuItem("home", url="home", icon="home"),
            MenuItem("projects", url="projects:project_list", icon="briefcase"),
            MenuItem("tasks", url="tasks:task_list", icon="check"),
            MenuItem("tags", url="tags:tag_list", icon="tags"),
        ],
        'extra': [
            MenuItem("test", url="test", icon="eye-open", position="extra"),
            MenuItem("commands", url="commands", icon="bullhorn", position="extra"),
        ],
        'settings': [
            MenuItem("test", url="test", icon="eye-open", position="extra"),
            MenuItem("commands", url="commands", icon="bullhorn", position="extra"),
        ],
    }
    return {'menu_items': menu_items}
