from django.db import models

# Create your models here.
from django.template import Template, Context
from django.template.loader import render_to_string


class Element:
    meta_template = 'styleguide/atoms/meta.html'

    def __init__(self, name, tag=None, template=None, context={}, **kwargs):
        if not (tag or template):
            raise Exception('Element `{}` needs a tag or template.'.format(name))
        self.name = name
        self.tag = tag
        self.template = template
        self.context = context

    def render_meta(self):
        context = {
            'name': self.name,
            'tag': self.tag,
            'template': self.template,
            'context': self.context,
        }
        template = self.meta_template
        return render_to_string(template, context=context)

    def render_element(self):
        template = self.template
        if template:
            return render_to_string(template, context=self.context)
        else:
            context = {self.tag: self.context}
            template = Template(
                '{{% load atoms_tags molecules_tags organisms_tags %}}{{% {tag} {tag}={tag} %}}'.format(tag=self.tag))
            return template.render(context=Context(context))

    def render(self):
        return self.render_meta() + self.render_element()

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
