from django.db import models

# Create your models here.
from django.template import Template, Context
from django.template.loader import render_to_string


class Element:
    meta_template = 'styleguide/atoms/meta.html'

    def __init__(self, name, tag=None, libraries=None, template=None, context={}, columns=0, **kwargs):
        if not (tag or template):
            raise Exception('Element `{}` needs a tag or template.'.format(name))
        self.name = name
        self.tag = tag
        self.libraries = libraries
        self.template = template
        self.context = context
        self.columns = columns

    def render_meta(self):
        context = {
            'name': self.name,
            'tag': self.tag,
            'libraries': self.libraries,
            'template': self.template,
            'context': self.context,
        }
        template = self.meta_template
        return render_to_string(template, context=context)

    def render_element(self):
        template = self.template
        if template:
            outcome = render_to_string(template, context=self.context)
        else:
            context = {self.tag: self.context}
            template = Template(
                '{{% load atoms_tags molecules_tags organisms_tags {libraries} %}}{{% {tag} {tag}={tag} %}}'.format(tag=self.tag, libraries=self.libraries))
            outcome = template.render(context=Context(context))
        return outcome

    def render(self):
        outcome = self.render_meta() + self.render_element()
        if self.columns:
            template = Template(
                '<div class="row"><div class="col-xs-{columns}">{{{{ outcome }}}}</div></div>'.format(columns=self.columns)
            )
            context = Context({'outcome': outcome})
            outcome = template.render(context=context)
        return outcome

    def __str__(self):
        return self.name


class ElementGroup(Element):
    template = 'styleguide/molecules/elements.html'
    is_group = True

    def __init__(self, name, columns=12, elements=[], **kwargs):
        context = {'columns': columns, 'elements': elements}
        super().__init__(name, template=self.template, context=context)

    def render_meta(self):
        context = {
            'name': self.name,
            # 'tag': self.tag,
            # 'template': self.template,
            # 'context': self.context,
        }
        template = self.meta_template
        return render_to_string(template, context=context)

    def append(self, element):
        self.context.get('elements', []).append(element)
