# Custom extensions to django-crispy-forms.
from crispy_forms.layout import Button, HTML
from django.template.loader import render_to_string

__author__ = 'eraldo'


class IconButton(Button):
    template = "lib/_crispy_icon_button.html"

    def __init__(self, name, value, icon, input_type="button", **kwargs):
        self.input_type = input_type
        super().__init__(name, value, **kwargs)
        self.icon = icon


class SaveButton(IconButton):
    input_type = "submit"

    def __init__(self):
        super().__init__('save', 'Save', 'save', input_type="submit", css_class="save-button btn-primary")


class CancelButton(HTML):
    def __init__(self):
        self.html = render_to_string("lib/_cancel_button.html")
