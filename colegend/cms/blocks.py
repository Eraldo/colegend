import inspect

from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from wagtail.core import blocks
from wagtail.core.blocks import RawHTMLBlock, StructBlock
from wagtail.embeds.blocks import EmbedBlock as WagtailEmbedBlock
from wagtail.images.blocks import ImageChooserBlock

from colegend.core.templatetags.core_tags import image


class HeadingBlock(blocks.CharBlock):
    class Meta:
        classname = 'full title'
        icon = 'title'
        template = 'widgets/heading.html'

    def get_context(self, value, parent_context=None):
        context = super().get_context(value)
        context['level'] = 1
        context['content'] = value
        return context


class RichTextBlock(blocks.RichTextBlock):
    class Meta:
        icon = 'pilcrow'
        template = 'widgets/richtext.html'

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context)
        context['content'] = value
        return context


class ImageBlock(ImageChooserBlock):
    class Meta:
        icon = 'image'
        template = 'widgets/image.html'

    def render(self, value, context=None):
        context = self.get_context(value, context)
        return image(
            url=context.get('url'),
            name=context.get('name'),
        )

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context)
        context['url'] = value.get_rendition('max-1200x1200').url
        context['name'] = value.title
        return context


class EmbedBlock(WagtailEmbedBlock):
    class Meta:
        icon = 'media'
        template = 'widgets/embed.html'

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context)
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

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context)
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

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context)
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
