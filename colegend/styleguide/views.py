import pprint
from django.template.defaultfilters import slugify
from django.template.loader import render_to_string
from django.views.generic import TemplateView
from .data import atoms_data, molecules_data, organisms_data


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

        # TODO: Split in sub-methods

        atoms = []
        for atom, data in sorted(atoms_data.items()):
            template = data.get('template')
            item_context = data.get('context')

            # Create rendering for meta data
            meta_context = {
                'name': atom,
                'template': template,
                'context': pprint.pformat(item_context),
            }

            item_meta = render_to_string("styleguide/atoms/meta.html", context=meta_context)
            context[atom + "_meta"] = item_meta

            item_output = render_to_string(template, context=item_context)
            context[atom + "_output"] = item_output

            context[atom] = item_meta + item_output
            atoms.append(item_meta + item_output)
        context['atoms'] = atoms
        return context
