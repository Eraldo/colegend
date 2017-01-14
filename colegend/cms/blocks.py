import inspect

from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from wagtail.wagtailcore import blocks
from wagtail.wagtailcore.blocks import RawHTMLBlock, StructBlock
from wagtail.wagtailembeds.blocks import EmbedBlock as WagtailEmbedBlock
from wagtail.wagtailimages.blocks import ImageChooserBlock

from colegend.core.templatetags.core_tags import image


class RequestBlockMixin:
    @staticmethod
    def accepts_context(func):
        """
        Helper function used by _render_with_context and _render_basic_with_context. Return true
        if the callable 'func' accepts a 'context' keyword argument
        """
        signature = inspect.signature(func)
        try:
            signature.bind_partial(context=None)
            return True
        except TypeError:
            return False

    def render(self, value, context=None):
        """
        Return a text rendering of 'value', suitable for display on templates. By default, this will
        use a template (with the passed context, supplemented by the result of get_context) if a
        'template' property is specified on the block, and fall back on render_basic otherwise.
        """
        template = getattr(self.meta, 'template', None)
        if not template:
            return self.render_basic(value, context=context)

        if self.accepts_context(self.get_context):
            new_context = self.get_context(value, context)
        else:
            new_context = dict(context)
            new_context.update(self.get_context(value))

        return mark_safe(render_to_string(template, new_context))

    def get_context(self, value, context=None):
        """
        Return a dict of context variables (derived from the block value, or otherwise)
        to be added to the template context when rendering this value through a template.
        """
        context = context or {}
        context.update({
            'self': value,
            self.TEMPLATE_VAR: value,
        })
        return context


class HeadingBlock(blocks.CharBlock):
    class Meta:
        classname = 'full title'
        icon = 'title'
        template = 'widgets/heading.html'

    def get_context(self, value):
        context = super().get_context(value)
        context['level'] = 1
        context['content'] = value
        return context


class RichTextBlock(blocks.RichTextBlock):
    class Meta:
        icon = 'pilcrow'
        template = 'widgets/richtext.html'

    def get_context(self, value):
        context = super().get_context(value)
        context['content'] = value
        return context


class ImageBlock(RequestBlockMixin, ImageChooserBlock):
    class Meta:
        icon = 'image'
        template = 'widgets/image.html'

    def render(self, value, context=None):
        context = self.get_context(value, context)
        return image(
            url=context.get('url'),
            name=context.get('name'),
        )

    def get_context(self, value, context=None):
        context = super().get_context(value, context)
        context['url'] = value.get_rendition('max-1200x1200').url
        context['name'] = value.title
        return context


class EmbedBlock(WagtailEmbedBlock):
    class Meta:
        icon = 'media'
        template = 'widgets/embed.html'

    def get_context(self, value):
        context = super().get_context(value)
        embed = value
        context['embed'] = embed
        return context


BASE_BLOCKS = [
    ('heading', HeadingBlock()),
    ('rich_text', RichTextBlock()),
    ('image', ImageBlock()),
    ('embed', EmbedBlock()),
    ('html', RawHTMLBlock()),
]


class SectionBlock(StructBlock):
    content = blocks.StreamBlock(BASE_BLOCKS)

    def get_context(self, value):
        context = super().get_context(value)
        context['content'] = value.get('content')
        return context

    class Meta:
        icon = 'fa fa-square-o'
        label = 'Section'
        template = 'widgets/section.html'


SECTION_BLOCKS = [
    ('section', SectionBlock()),
]

CMS_BLOCKS = BASE_BLOCKS + SECTION_BLOCKS


class ColumnsBlock(StructBlock):
    left_column = blocks.StreamBlock(BASE_BLOCKS)
    right_column = blocks.StreamBlock(BASE_BLOCKS, form_classname='pull-right')

    def get_context(self, value):
        context = super().get_context(value)
        context['left_column'] = value.get('left_column')
        context['right_column'] = value.get('right_column')
        return context

    class Meta:
        icon = 'fa fa-columns'
        label = 'Columns 1-1'
        template = None


class Columns1To1Block(ColumnsBlock):
    class Meta:
        label = 'Columns 1:1'
        template = 'widgets/columns-1-1.html'


class Columns1To2Block(ColumnsBlock):
    class Meta:
        label = 'Columns 1:2'
        template = 'widgets/columns-1-2.html'


class Columns2To1Block(ColumnsBlock):
    class Meta:
        label = 'Columns 2:1'
        template = 'widgets/columns-2-1.html'


COLUMN_BLOCKS = [
    ('columns_1_to_1', Columns1To1Block()),
    ('columns_1_to_2', Columns1To2Block()),
    ('columns_2_to_1', Columns2To1Block()),
]

CMS_BLOCKS += COLUMN_BLOCKS


# class BlockFactory:
#     base_blocks = [HeadingBlock, RichTextBlock, ImageBlock, EmbedBlock]
#     extra_blocks = [RawHTMLBlock]
#
#     def get_blocks(self):
#         print()
#
#     @classmethod
#     def camelcase_to_underscores(name):
#         """
#         Taken from a github page:
#         http://stackoverflow.com/questions/1175208/elegant-python-function-to-convert-camelcase-to-snake-case
#         """
#         s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
#         return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()
