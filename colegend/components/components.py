from django import template
from django.template.library import parse_bits
from django.utils.decorators import classonlymethod
from django.utils.inspect import getargspec

from colegend.components.utils import camelcase_to_underscores


class ComponentNode(template.Node):
    def __init__(self, component):
        self.component = component
        # Needed for template tag naming.
        self.__name__ = component.name

    def __call__(self, parser, token):
        """
        Pretending to be a callable function to as as a template tag.
        Used by the template library.
        :param parser:
        :param token:
        :return:
        """
        self.args, self.kwargs, self.variable = self.parse_content(parser, token)
        return self

    @property
    def _decorated_function(self):
        return self

    def render(self, context):
        """
        Used by the template Node. (overwrite)
        :param context:
        :return:
        """
        args, kwargs = self.get_resolved_arguments(context, self.args, self.kwargs)
        if self.takes_context:
            output = self.component.render(context, *args, **kwargs)
        else:
            output = self.component.render(*args, **kwargs)

        variable = self.variable
        if variable:
            context[variable] = output
            return ''
        else:
            return output

    @staticmethod
    def get_resolved_arguments(context, args, kwargs):
        resolved_args = [var.resolve(context) for var in args]
        resolved_kwargs = {k: v.resolve(context) for k, v in kwargs.items()}
        return resolved_args, resolved_kwargs

    def parse_content(self, parser, token):
        """
        This is called to parse the incoming context.

        It's return value will be set to self.args, self.kwargs, self.variable
        """
        bits = token.split_contents()[1:]
        target_var = None

        if len(bits) >= 2 and bits[-2] == 'as':
            target_var = bits[-1]
            bits = bits[:-2]

        params, varargs, varkw, defaults = getargspec(self.component.render)

        if params[0] == 'context':
            takes_context = True
        else:
            takes_context = False
        self.takes_context = takes_context

        function_name = self.component.name
        args, kwargs = parse_bits(
            parser, bits, params, varargs, varkw, defaults,
            takes_context, function_name
        )
        return args, kwargs, target_var


class Component:
    """
    Django component that can be used as a template tag.

    Subclasses should define ``render()``.

    The template tag is automatically named based on the class name.
    """

    @property
    def name(self):
        """
        Returns the name of the class in underscore style.
        If the class name includes the word 'Component', it will be removed
        before conversion.

        Example:
        class DemoComponent => 'demo'
        MyDemoComponent => 'my_demo'
        FooBar => 'foo_bar'

        :return: The name for the template tag to use in the template.
        """
        class_name = self.__class__.__name__
        camel_name = class_name.replace('Component', '')
        name = camelcase_to_underscores(camel_name)
        return name

    @classonlymethod
    def as_tag(cls):
        return ComponentNode(component=cls())

    def render(self, context, *args, **kwargs):
        """
        This is called to return a node to the template.

        It should return set things in the context or return
        whatever representation is appropriate for the template.
        """
        raise NotImplementedError
