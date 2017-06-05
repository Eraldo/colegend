from django.shortcuts import redirect
from wagtail.wagtailcore.models import Page


class OfficePage(Page):
    template = 'office/base.html'

    def serve(self, request, *args, **kwargs):
        return redirect(self.get_first_child().url)

    parent_page_types = ['cms.RootPage']
    subpage_types = ['AgendaPage', 'ActionPage', 'InboxPage', 'OutcomesPage']


class AgendaPage(Page):
    template = 'office/agenda.html'

    parent_page_types = ['OfficePage']
    subpage_types = []

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        return context

    def __str__(self):
        return self.title


class ActionPage(Page):
    template = 'office/action.html'

    parent_page_types = ['OfficePage']
    subpage_types = []

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        return context

    def __str__(self):
        return self.title


class InboxPage(Page):
    template = 'office/inbox.html'

    parent_page_types = ['OfficePage']
    subpage_types = []

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        return context

    def __str__(self):
        return self.title


class OutcomesPage(Page):
    template = 'office/outcomes.html'

    parent_page_types = ['OfficePage']
    subpage_types = []

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        return context

    def __str__(self):
        return self.title
