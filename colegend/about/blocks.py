# from wagtail.core import blocks
#
# from colegend.cms.blocks import BASE_BLOCKS, SectionBlock, Columns1To1Block
#
# # LogoBlock
#
# BASE_BLOCKS += [
#     # ('logo', LogoBlock()),
# ]
#
#
# class SectionBlock(SectionBlock):
#     content = blocks.StreamBlock(BASE_BLOCKS)
#
#
# class Columns1To1Block(Columns1To1Block):
#     left_column = blocks.StreamBlock(BASE_BLOCKS)
#     right_column = blocks.StreamBlock(BASE_BLOCKS, form_classname='pull-right')
#
#
# BLOCKS = BASE_BLOCKS + [
#     ('section', SectionBlock()),
#     ('columns_1_to_1', Columns1To1Block()),
# ]
