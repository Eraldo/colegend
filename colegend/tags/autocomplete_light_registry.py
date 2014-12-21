import autocomplete_light
from django.core.urlresolvers import reverse
from django.template.loader import render_to_string
from django.utils.html import escape
from tags.models import Tag

__author__ = 'eraldo'


class TagAutocomplete(autocomplete_light.AutocompleteModelBase):
    model = Tag
    search_fields = ['name']
    choice_html_format = '<div data-value="{value}"><span class="remove"><span onclick="javascript:return false;">{tag}</span></span></div>'
    add_another_url_name = "tags:tag_new"

    attrs = {
        'placeholder': 'Add Tags here..',
    }

    def choices_for_request(self):
        self.choices = self.request.user.tags
        return super().choices_for_request()

    def choice_html(self, choice):
        return self.choice_html_format.format(
            value=escape(self.choice_value(choice)),
            tag=render_to_string("tags/_tag.html", dictionary={"tag": choice})
        )


autocomplete_light.register(Tag, TagAutocomplete)
