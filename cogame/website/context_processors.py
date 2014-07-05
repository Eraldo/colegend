from bootstrap3.components import render_icon
from django.utils.safestring import mark_safe

__author__ = 'eraldo'


class MenuItem:
    def __init__(self, name, url, icon=None):
        self.name = name
        self.url = url
        if icon:
            icon = mark_safe(render_icon(icon))
        self.icon = icon

    def __str__(self):
        return self.name


def menu(request):
    "A context processor that provides a menu with 'menu_item's."

    return {
        # name, url
        'menu_items': [
            MenuItem("home", url="home", icon="home"),
            MenuItem("projects", url="projects:project_list", icon="briefcase"),
            MenuItem("tasks", url="tasks:task_list", icon="check"),
            MenuItem("tags", url="tags:tag_list", icon="tags"),
            MenuItem("test", url="test", icon="eye-open"),
            MenuItem("commands", url="commands", icon="bullhorn"),
        ]
    }

