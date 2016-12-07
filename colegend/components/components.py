from django import template
from django.template.library import parse_bits
from django.utils.inspect import getargspec

from colegend.components.utils import camelcase_to_underscores


class Component(template.Node):
    """
    Django template tag that that combines parsing and rendering

    Subclasses should define ``render_component()``.

    The tag is automatically named based on the class name.
    """
    name = ''
    takes_context = True

    def get_component_name(self):
        """
        Returns the given name if a name attribute was found.
        Otherwise it returns the name of the class in underscore style.
        If the class name includes the word 'Component', it will be removed
        before conversion.

        Example:
        class DemoComponent => 'demo'
        MyDemoComponent => 'my_demo'
        FooBar => 'foo_bar'

        :return: The name for the template tag to use in the template.
        """
        if self.name:
            name = self.name
        else:
            class_name = self.__class__.__name__
            camel_name = class_name.replace('Component', '')
            name = camelcase_to_underscores(camel_name)
            return name

    def __init__(self, *args, **kwargs):
        # self._decorated_function = 'foo'
        self.__name__ = self.get_component_name()

    def __call__(self, parser, token):
        """
        Pretending to be a callable function to as as a template tag.
        Used by the template library.
        :param parser:
        :param token:
        :return:
        """
        self.token = token
        self.parser = parser
        self.parsed = self.parse_content(self.parser, self.token)
        self.args, self.kwargs, self.variable = self.parsed
        return self

    def render(self, context):
        """
        Used by the template Node. (overwrite)
        :param context:
        :return:
        """
        self.context = context
        args, kwargs = self.get_resolved_arguments(context, self.args, self.kwargs)
        output = self.render_component(context, *args, **kwargs)
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
        params, varargs, varkw, defaults = getargspec(self.render_component)
        takes_context = self.takes_context
        function_name = self.name
        args, kwargs = parse_bits(
            parser, bits, params, varargs, varkw, defaults,
            takes_context, function_name
        )
        return args, kwargs, target_var

    def render_component(self, context, *args, **kwargs):
        """
        This is called to return a node to the template.

        It should return set things in the context or return
        whatever representation is appropriate for the template.
        """
        raise NotImplementedError
