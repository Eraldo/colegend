from bootstrap3.components import render_icon

__author__ = 'eraldo'


def menu(request):
    "A context processor that provides a menu with 'menu_item's."

    return {
        # name, url
        'menu_items': (
            (render_icon("home"), 'home'),
            (render_icon("briefcase"), 'projects:project_list'),
            (render_icon("check"), 'tasks:task_list'),
            (render_icon("tags"), 'tags:tag_list'),
            (render_icon("eye-open"), 'test'),
            (render_icon("asterisk"), 'commands'),
        )
    }

