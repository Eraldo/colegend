from django.db import models

# Create your models here.
from django.template import Template, Context
from django.template.defaultfilters import slugify
from django.template.loader import render_to_string


class Widget:
    meta_template = 'styleguide/widgets/meta.html'
    widgets = {}

    def __init__(self, name, tag=None, libraries=None, parameters={}, template=None, context={}, columns=0, **kwargs):
        if not (tag or template):
            raise Exception('Widget `{}` needs a tag or template.'.format(name))
        self.name = name
        self.tag = tag
        self.libraries = libraries
        self.parameters = parameters
        self.template = template
        self.context = context
        self.columns = columns
        self.widgets[slugify(name)] = self

    def render_meta(self):
        context = {
            'name': self.name,
            'tag': self.tag,
            'libraries': self.libraries,
            'parameters': self.parameters,
            'template': self.template,
            'context': self.context,
        }
        template = self.meta_template
        return render_to_string(template, context=context)

    def render_widget(self):
        template = self.template
        if template:
            outcome = render_to_string(template, context=self.context)
        else:
            template = Template(
                '{{% load {libraries} %}}{{% {tag} {parameters} %}}'.format(
                    tag=self.tag,
                    libraries=self.libraries,
                    parameters=' '.join('{name}={name}'.format(name=name) for name in self.parameters.keys())
                )
            )
            outcome = template.render(context=Context(self.parameters))
        return outcome

    def render(self):
        outcome = self.render_meta() + self.render_widget()
        if self.columns:
            template = Template(
                '<div class="row"><div class="col-xs-{columns}">{{{{ outcome }}}}</div></div>'.format(
                    columns=self.columns)
            )
            context = Context({'outcome': outcome})
            outcome = template.render(context=context)
        return outcome

    @classmethod
    def get(cls, name):
        widget = cls.widgets.get(slugify(name))
        if widget:
            return widget.render_widget()
        raise Exception('Widget "{}" not found.'.format(name))

    def __str__(self):
        return self.name


class WidgetGroup(Widget):
    template = 'styleguide/widgets/widgets.html'
    is_group = True

    def __init__(self, name, columns=12, widgets=[], **kwargs):
        context = {'columns': columns, 'widgets': widgets}
        super().__init__(name, template=self.template, context=context)

    def render_meta(self):
        context = {
            'name': self.name,
        }
        template = self.meta_template
        return render_to_string(template, context=context)

    def append(self, widget):
        self.context.get('widgets', []).append(widget)
