from django.template.defaultfilters import slugify
from django.views.generic import TemplateView

from .data import widgets


class StyleguideView(TemplateView):
    """
    A 'styleguide' django view.
    """
    template_name = 'styleguide/index.html'

    def get_template_names(self):
        template_name = self.kwargs.get('template')
        if template_name:
            return ['styleguide/demos/{}.html'.format(slugify(template_name))]
        return super().get_template_names()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['widgets'] = widgets
        return context
