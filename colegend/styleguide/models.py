from collections import OrderedDict

from django.contrib.sites.models import Site
from django.template import Template, Context
from django.template.defaultfilters import slugify
from django.template.loader import render_to_string
from django.test import RequestFactory


class BaseWidget:
    meta_template = 'styleguide/widgets/meta.html'
    widget_template = 'styleguide/widgets/widget.html'
    widgets = OrderedDict()

    def __init__(self, name, columns=12, comment=None, **kwargs):
        self.name = name
        self.columns = columns
        self.widgets[slugify(name)] = self
        self.comment = comment

    def get_meta_kwargs(self):
        if hasattr(self, 'meta_kwargs'):
            return self.meta_kwargs
        else:
            return {}

    def render_meta(self):
        context = {
            'name': self.name,
            'comment': self.comment,
        }
        context.update({'meta': self.get_meta_kwargs()})
        template = self.meta_template
        return render_to_string(template, context=context)

    def render(self):
        raise NotImplementedError()

    def render_widget(self):
        request = RequestFactory().get('/')
        request.site = Site.objects.get_current()
        context = {
            'meta': self.render_meta(),
            'widget': self.render(),
            'columns': self.columns,
            'request': request,
        }
        return render_to_string(self.widget_template, context=context)

    @classmethod
    def get(cls, name):
        widget = cls.widgets.get(slugify(name))
        if widget:
            return widget.render()
        raise Exception('Widget "{}" not found.'.format(name))

    def __str__(self):
        return self.name


class Widget(BaseWidget):
    def __init__(self, name, template, context={}, **kwargs):
        self.template = template
        request = RequestFactory().get('/')
        request.site = Site.objects.get_current()
        context['request'] = request
        self.context = context
        super().__init__(name, **kwargs)

    def get_meta_kwargs(self):
        kwargs = OrderedDict({
            'template': self.template,
            'context': self.context,
        })
        return kwargs

    def render(self):
        return render_to_string(self.template, context=self.context)


class TagWidget(BaseWidget):
    def __init__(self, name, tag, libraries='core_tags', parameters={}, **kwargs):
        self.tag = tag
        self.parameters = parameters
        self.libraries = libraries
        super().__init__(name, **kwargs)

    def get_meta_kwargs(self):
        kwargs = OrderedDict({
            'tag': self.tag,
            'parameters': self.parameters,
            'libraries': self.libraries,
        })
        return kwargs

    def render(self):
        return render_to_string(self.template, context=self.context)

    def render(self):
        template = Template(
            '{{% load {libraries} %}}{{% {tag} {parameters} %}}'.format(
                tag=self.tag,
                libraries=self.libraries,
                parameters=' '.join('{name}={name}'.format(name=name) for name in self.parameters.keys())
            )
        )
        outcome = template.render(context=Context(self.parameters))
        return outcome


class WidgetGroup(Widget):
    def __init__(self, name, widgets=[], columns=12, **kwargs):
        template = 'styleguide/widgets/widgets.html'
        self.group_widgets = widgets
        context = {'columns': columns, 'widgets': widgets}
        super().__init__(name, template=template, context=context, **kwargs)

    def get_meta_kwargs(self):
        kwargs = OrderedDict({
            'widgets': ', '.join([str(widget) for widget in self.group_widgets]),
            'columns': self.columns,
        })
        return kwargs
