from django.template import Context
from django.template.defaultfilters import slugify
from django.views.generic import TemplateView

from .models import Element
from .data import atoms, molecules, organisms

from .templatetags.atoms_tags import label


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
        context['atoms'] = atoms
        context['organisms'] = organisms
        context['molecules'] = molecules

        label1 = Element('Test Label', tag='label', context={'text': 'foo', 'class': 'bg-main'})
        label2 = Element('Test Label 2', tag='label', context={'text': label1.render_element()})

        from django.templatetags.static import static
        logo = Element('Logo', template='atoms/logo.html', context={'url': static('images/coLegendLogo_86x18.png')})

        context['elements'] = [label1, label2, logo]
        # data = {'text': 'foo', 'class': 'bg-main'}
        # label1 = label(context, data)
        # label1.data = data
        # context['element'] = label1
        #
        # data = {'text': label1}
        # label2 = label(context, data)
        # label2.data = data
        # context['element2'] = label2

        return context
