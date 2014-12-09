# Custom extensions to django-crispy-forms.
from crispy_forms.layout import Button, HTML

__author__ = 'eraldo'


class IconButton(Button):
    template = "lib/_crispy_icon_button.html"

    def __init__(self, name, value, icon, **kwargs):
        super().__init__(name, value, **kwargs)
        self.icon = icon


class SaveButton(IconButton):
    input_type = "submit"

    def __init__(self):
        super().__init__('save', 'Save', 'save', input_type="submit", css_class="btn-primary")


class CancelButton(HTML):
    def __init__(self):
        self.html = """{% load icons %}<a href="javascript:history.go(-1)" class="btn btn-default">{% icon "cancel" %} Cancel</a>"""
