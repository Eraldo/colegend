import autocomplete_light
from django.core.urlresolvers import reverse
from django.template.loader import render_to_string
from django.utils.html import escape
from projects.models import Project

__author__ = 'eraldo'


class ProjectAutocomplete(autocomplete_light.AutocompleteModelBase):
    model = Project
    search_fields = ['name']
    choice_html_format = '<div data-value="{value}"><span class="remove"><span onclick="javascript:return false;">{tag}</span></span></div>'
    empty_html_format = render_to_string("autocomplete_light/_empty_create.html", {"url": reverse("projects:project_new")})

    attrs = {
        'placeholder': 'Choose project..',
    }

    def choices_for_request(self):
        self.choices = self.request.user.projects
        return super().choices_for_request()

    def choice_html(self, choice):
        return self.choice_html_format.format(
            value=escape(self.choice_value(choice)),
            tag=render_to_string("projects/_project_link.html", dictionary={"project": choice})
        )


autocomplete_light.register(Project, ProjectAutocomplete)
