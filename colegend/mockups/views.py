from django.contrib.auth.mixins import LoginRequiredMixin
from django.template.defaultfilters import slugify
from django.views.generic import TemplateView


class MockupView(LoginRequiredMixin, TemplateView):
    def get_template_names(self):
        mockup_name = self.kwargs.get('template')
        return ['mockups/{}.html'.format(slugify(mockup_name))]
