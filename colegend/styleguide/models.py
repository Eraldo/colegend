from django.template.defaultfilters import slugify
from django.template.loader import render_to_string


class BaseWidget:
    meta_template = 'styleguide/widgets/meta.html'
    widget_template = 'styleguide/widgets/widget.html'
    widgets = {}

    def __init__(self, name, columns=12, **kwargs):
        self.name = name
        self.columns = columns
        self.widgets[slugify(name)] = self

    def get_meta_kwargs(self):
        if hasattr(self, 'meta_kwargs'):
            return self.meta_kwargs
        else:
            return {}

    def render_meta(self):
        context = {
            'name': self.name,
        }
        context.update({'meta': self.get_meta_kwargs()})
        template = self.meta_template
        return render_to_string(template, context=context)

    def render(self):
        raise NotImplementedError()

    def render_widget(self):
        context = {
            'meta': self.render_meta(),
            'widget': self.render(),
            'columns': self.columns,
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
        self.context = context
        super().__init__(name, **kwargs)

    def get_meta_kwargs(self):
        kwargs = {
            'template': self.template,
            'context': self.context,
        }
        return kwargs

    def render(self):
        return render_to_string(self.template, context=self.context)


# class TagWidget(Widget):
#     meta_template = 'styleguide/widgets/widgets.html'
#
#     def __init__(self, name, tag, libraries='core_tags', parameters={}, **kwargs):
#         self.tag = tag
#         self.parameters = parameters
#         self.libraries = libraries
#         super().__init__(name, **kwargs)
#
#     def render_meta(self):
#         context = {
#             'name': self.name,
#         }
#         template = self.meta_template
#         return render_to_string(template, context=context)
#
#     def append(self, widget):
#         self.context.get('widgets', []).append(widget)


class WidgetGroup(Widget):
    is_group = True

    def __init__(self, name, widgets=[], columns=12, **kwargs):
        template = 'styleguide/widgets/widgets.html'
        self.group_widgets = widgets
        context = {'columns': columns, 'widgets': widgets}
        super().__init__(name, template=template, context=context, **kwargs)

    def get_meta_kwargs(self):
        kwargs = {
            'columns': self.columns,
            'widgets': ', '.join([str(widget) for widget in self.group_widgets]),
        }
        return kwargs
