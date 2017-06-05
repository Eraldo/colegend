from django.shortcuts import redirect
from wagtail.wagtailcore.models import Page


class ArcadePage(Page):
    template = 'arcade/base.html'

    def serve(self, request, *args, **kwargs):
        return redirect(self.get_first_child().url)

    parent_page_types = ['cms.RootPage']
    subpage_types = ['AdventuresPage', 'GamesPage', 'ContestsPage', 'ShopPage']


class AdventuresPage(Page):
    template = 'arcade/adventures.html'

    parent_page_types = ['ArcadePage']
    subpage_types = []

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        return context

    def __str__(self):
        return self.title


class GamesPage(Page):
    template = 'arcade/games.html'

    parent_page_types = ['ArcadePage']
    subpage_types = []

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        return context

    def __str__(self):
        return self.title


class ContestsPage(Page):
    template = 'arcade/contests.html'

    parent_page_types = ['ArcadePage']
    subpage_types = []

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        return context

    def __str__(self):
        return self.title


class ShopPage(Page):
    template = 'arcade/shop.html'

    parent_page_types = ['ArcadePage']
    subpage_types = []

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        return context

    def __str__(self):
        return self.title
