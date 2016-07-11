from classytags.arguments import Argument
from classytags.core import Options
from classytags.helpers import InclusionTag
from django import template
from django.template.defaultfilters import slugify
from wagtail.wagtailimages.templatetags.wagtailimages_tags import image as wagtail_image

from colegend.core.templatetags.core_tags import link

register = template.Library()


@register.tag
class TableOfContents(InclusionTag):
    name = 'toc'
    template = 'cms/widgets/table-of-contents.html'
    options = Options(
        Argument('headings', required=False),
    )

    def render_tag(self, context, **kwargs):
        nodes = self.get_context(context, **kwargs).get('nodes')
        if nodes:
            return super().render_tag(context, **kwargs)
        else:
            return ''

    def get_context(self, context, **kwargs):
        headings = kwargs.get('headings')
        if not headings:
            page = context.get('page')
            if page and hasattr(page, 'content'):
                headings = [block.value for block in page.content if block.block_type == 'heading']
        nodes = []
        if headings and len(headings) > 1:
            nodes = [link(heading, url='#{}'.format(slugify(heading))) for heading in headings]
        return {
            'nodes': nodes,
        }


@register.tag
class Menu(InclusionTag):
    name = 'menu'
    template = 'widgets/navigation.html'
    options = Options(
        Argument('root', required=False),
    )

    # def get_node(self, page, current_page, ancestors):
    #     return {
    #         'text': page.title,
    #         'href': page.url if not page == current_page else None,
    #     }
    #
    # def get_nodes(self, context):
    #     current_page = context.get('page')
    #     if current_page:
    #         current_page = current_page.specific
    #         ancestors = current_page.get_ancestors().live().in_menu().specific()
    #         return [self.get_node(page, current_page=current_page, ancestors=ancestors) for page in ancestors] + [
    #             self.get_node(current_page, current_page=current_page, ancestors=ancestors)]
    #     else:
    #         return []

    def get_context(self, context, root, **kwargs):
        nodes = []
        if root:
            pages = root.get_children().live().in_menu()
            nodes = pages
        return {
            'nodes': nodes,
            'page': context.get('page'),
        }


@register.tag(name="cms_image")
def cms_image(parser, token):
    return wagtail_image(parser, token)

# @register.tag
# class Breadcrumb(InclusionTag):
#     name = 'breadcrumb'
#     template = 'widgets/breadcrumb.html'
#
#     def get_node(self, page, current_page, ancestors):
#         return {
#             'text': page.title,
#             'href': page.url if not page == current_page else None,
#         }
#
#     def get_nodes(self, context):
#         current_page = context.get('page')
#         if current_page:
#             current_page = current_page.specific
#             ancestors = current_page.get_ancestors().live().in_menu().specific()
#             return [self.get_node(page, current_page=current_page, ancestors=ancestors) for page in ancestors] + [
#                 self.get_node(current_page, current_page=current_page, ancestors=ancestors)]
#         else:
#             return []
#
#     def get_context(self, context, **kwargs):
#         nodes = self.get_nodes(context)
#         return {'links': nodes}
