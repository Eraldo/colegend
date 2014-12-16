from django import template
from django.templatetags.static import static

__author__ = 'eraldo'

register = template.Library()

mousetrap_base_url = static("website/bower_components/mousetrap/")
plugins = ["global-bind"]

BINDINGS = [
    {
        'keys': '?',
        'command': 'keyboard_help()',
    },
    {
        'keys': 'esc',
        'command': 'keyboard_deselect()',
        'is_global': True,  # global binding
    },
    {
        'keys': 'r',
        'command': 'keyboard_refresh()',
    },
    {
        'keys': 'm',
        'command': 'keyboard_menu()',
    },
    {
        'keys': 'M',
        'command': 'keyboard_menu(main=true)',
    },

    {
        'keys': 'n',
        'command': 'keyboard_new()',
    },
    {
        'keys': ['o', 'enter'],
        'command': 'keyboard_show()',
    },
    {
        'keys': 'e',
        'command': 'keyboard_edit()',
    },
    {
        'keys': 'd',
        'command': 'keyboard_delete()',
    },
    {
        'keys': 'c',
        'command': 'keyboard_complete()',
    },

    {
        'keys': 's',
        'command': 'keyboard_save()',
    },
    {
        'keys': 'x',
        'command': 'keyboard_cancel()',
    },

    {
        'keys': ['k', 'up'],
        'command': 'keyboard_navigate("up");',
    },
    {
        'keys': ['j', 'down'],
        'command': 'keyboard_navigate("down");',
    },

    # PATHS (gmail style key sequences)

    # Operator
    {
        'keys': 'g m',  # go contact
        'command': 'contact-menu-item',
        'action': 'link_id'
    },
    {
        'keys': 'g n',  # go news
        'command': 'news-menu-item',
        'action': 'link_id'
    },
    {
        'keys': 'g ?',  # go tutorials
        'command': 'tutorials-menu-item',
        'action': 'link_id'
    },
    {
        'keys': 'g s',  # go search
        'command': 'search-menu-item',
        'action': 'link_id'
    },
    {
        'keys': 'g h',  # go home
        'command': 'home-menu-item',
        'action': 'link_id'
    },


    {
        'keys': 'g u',  # go profile
        'command': 'profile-menu-item',
        'action': 'link_id'
    },
    {
        'keys': 'g *',  # go settings
        'command': 'settings-menu-item',
        'action': 'link_id'
    },
    {
        'keys': 'g b',  # go back
        'command': 'javascript:history.go(-1);',
    },


    # Mentor
    {
        'keys': 'g j',  # go journal
        'command': 'journal-menu-item',
        'action': 'link_id'
    },
    {
        'keys': 'g g',  # go gatherings
        'command': 'gatherings-menu-item',
        'action': 'link_id'
    },
    {
        'keys': 'g c',  # go challenges
        'command': 'challenges-menu-item',
        'action': 'link_id'
    },
    {
        'keys': 'g d',  # go dojo
        'command': 'dojo-menu-item',
        'action': 'link_id'
    },
    {
        'keys': 'g v',  # go vision
        'command': 'life-vision-menu-item',
        'action': 'link_id'
    },

    # Manager
    {
        'keys': 'g a',  # go agenda
        'command': 'agenda-menu-item',
        'action': 'link_id'
    },
    {
        'keys': 'g p',  # go projects
        'command': 'projects-menu-item',
        'action': 'link_id'
    },
    {
        'keys': 'g t',  # go tasks
        'command': 'tasks-menu-item',
        'action': 'link_id'
    },
    {
        'keys': 'g x',  # go tags
        'command': 'tags-menu-item',
        'action': 'link_id'
    },

    # Motivator
    {
        'keys': 'g l',  # go legend
        'command': 'legend-menu-item',
        'action': 'link_id'
    },
    {
        'keys': 'g q',  # go quotes
        'command': 'quotes-menu-item',
        'action': 'link_id'
    },
    # {
    #     'keys': 'o down right left down right left',  # Saria's Song!
    #     'command': """alert("Saria's Song!");""",
    # },
    # {
    #     'keys': 'up up down down left right left right b a enter',  # KOWABUNGA!
    #     'command': 'alert("KOWABUNGA!");',
    # },
]


class Binding():
    def __init__(self, keys, command, action="js", is_global=False):
        valid_actions = (
            'js',  # javascript code
            # 'link',  # a url to navigate to
            "link_id",  # a html link id to follow it's href
        )
        if action not in valid_actions:
            raise ValueError("Invalid action: '{}'. Must be one of {}".format(action, valid_actions))
        if isinstance(keys, list):
            self.keys = keys
        else:
            self.keys = "'{}'".format(keys)
        if action == "link_id":
            self.command = 'visitLink("{link_id}");'.format(link_id=command)
            self.action = "js"
        else:
            self.command = command
            self.action = action
        self.is_global = is_global

    def render_javascript(self):
        action = self.action
        if action == "js":
            if self.is_global:
                function = "bindGlobal"
            else:
                function = "bind"
            javascript = "Mousetrap.{function}({keys}, function() {command});\n".format(
                function=function, keys=self.keys, command='{'+self.command+'}'
            )
        else:
            raise ValueError
        return javascript

    def __str__(self):
        return self.keys


def _render_bindings(bindings=[]):
    js = ''
    for binding in bindings:
        js += (Binding(**binding).render_javascript())
    return js

bindings = _render_bindings(BINDINGS)

@register.simple_tag
def keyboard_scripts():
    javascript = ''
    script_template = """<script src="{url}"></script>\n"""

    # add mousetrap

    mousetrap_url = mousetrap_base_url + "mousetrap.min.js"
    javascript += script_template.format(url=mousetrap_url)

    # add plugins

    plugin_base_url = mousetrap_base_url + "plugins/"
    for plugin in plugins:
        plugin_url = "{base}{plugin}/mousetrap-{plugin}.min.js".format(base=plugin_base_url, plugin=plugin)
        plugin_script = script_template.format(url=plugin_url)
        javascript += plugin_script

    # add helper functions

    visit_link = """
    function visitLink(link_id) {
        var url = $("#" + link_id).attr("href");
        window.open(url, "_self");
    };
"""
    javascript += '<script>{}</script>\n'.format(visit_link)

    return javascript


@register.simple_tag
def keyboard_bindings():
    javascript = bindings
    return "<script>\n{}</script>\n".format(javascript)


@register.simple_tag
def keyboard():
    """
    Return HTML for Mousetrap JavaScript
    """
    javascript = ''

    scripts = keyboard_scripts()
    if scripts:
        javascript += scripts

    bindings = keyboard_bindings()
    if bindings:
        javascript += bindings

    return javascript
