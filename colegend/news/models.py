from wagtail.wagtailcore.models import Page


class NewsPage(Page):
    template = 'news/base.html'

    # def serve(self, request, *args, **kwargs):
    #     return redirect(self.get_first_child().url)

    parent_page_types = ['cms.RootPage']
    subpage_types = []
