from wagtail.wagtailcore import blocks
from wagtail.wagtailcore.blocks import RawHTMLBlock, StructBlock
from wagtail.wagtailembeds.blocks import EmbedBlock as WagtailEmbedBlock
from wagtail.wagtailimages.blocks import ImageChooserBlock

from colegend.core.templatetags.core_tags import image


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


class ImageBlock(ImageChooserBlock):
    class Meta:
        icon = 'image'
        template = 'widgets/image.html'

    def render(self, value):
        context = self.get_context(value)
        return image(
            url=context.get('url'),
            name=context.get('name'),
        )

    def get_context(self, value):
        context = super().get_context(value)
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
]


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

ALL_BLOCKS = BASE_BLOCKS + COLUMN_BLOCKS


ALL_BLOCKS += [
    ('html', RawHTMLBlock()),
]


# class QABlock(StructBlock):
#     question = CharBlock()
#     answer = RichTextBlock()
#
#
# class FAQBlock(StructBlock):
#     title = CharBlock()
#     faqs = ListBlock(QABlock())
#
#     class Meta:
#         icon = 'fa fa-medkit'
#         template = 'blocks/faq_block.html'
#
#     def get_context(self, value):
#         context = super().get_context(value)
#         context['titel'] = value.get('title')
#         context['list'] = []
#         for faq in value.get('faqs'):
#             res = {'term': faq.get('question'),
#                    'definitions': [{'text': faq.get('answer')}],
#                    'opened': False,
#                    'notoggle': False
#                    }
#             context['list'] += [res]
#         return context

