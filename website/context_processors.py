__author__ = 'eraldo'


def menu(request):
    "A context processor that provides a menu with 'menu_item's."

    return {
        # name, url
        'menu_items': (
            ('home', 'home'),
            ('projects', 'projects:project_list'),
            ('tasks', 'tasks:task_list'),
            ('tags', 'tags:tag_list'),
            ('test', 'test'),
            ('commands', 'commands'),
        )
    }

