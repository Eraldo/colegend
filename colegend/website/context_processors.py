from django.utils.safestring import mark_safe

__author__ = 'eraldo'


class MenuItem:
    positions = ["main", "extra", "settings"]

    def __init__(self, name, url, arg=None, icon=None):
        self.name = name
        self.url = url
        self.arg = arg
        # add icon if given
        if icon:
            icon = mark_safe('<i class="fa fa-{}"></i>'.format(icon))
        self.icon = icon

    def __str__(self):
        return self.name


def menu(request):
    """A context processor that provides menu_items."""
    menu_items = {
        'mentor': [
            MenuItem("Life Vision", url="visions:vision_list", icon="eye"),
            MenuItem("Meetings", url="meetings", icon="comments-o"),
            MenuItem("Journal", url="journals:dayentry_list", icon="book"),
        ],
        'manager': [
            MenuItem("Projects", url="projects:project_list", icon="sitemap"),
            MenuItem("Tasks", url="tasks:task_list", icon="check-circle"),
            MenuItem("Tags", url="tags:tag_list", icon="tags"),
        ],
        'motivator': [
        ],
        'operator': [
            MenuItem("Contact", url="contact", icon="envelope"),
            MenuItem("About", url="about", icon="info-circle"),
            MenuItem("Features", url="features:feature_list", icon="road"),
            MenuItem("Home", url="home", icon="home"),
        ],
        'settings': [
            MenuItem("settings", url="users:detail", arg=request.user, icon="wrench"),
        ],
        'experimental': [
            MenuItem("routines", url="routines:routine_list", icon="stack-overflow"),
            MenuItem("habits", url="habits:habit_list", icon="link"),
            MenuItem("commands", url="commands", icon="bullhorn"),
        ],
        'admin': [
            MenuItem("test", url="test", icon="code"),
        ],
    }
    return {'menu_items': menu_items}
