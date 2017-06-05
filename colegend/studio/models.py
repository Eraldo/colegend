from django.shortcuts import redirect
from wagtail.wagtailcore.models import Page


class StudioPage(Page):
    template = 'studio/base.html'

    def serve(self, request, *args, **kwargs):
        return redirect(self.get_first_child().url)

    parent_page_types = ['cms.RootPage']
    subpage_types = ['journals.JournalPage', 'InterviewPage', 'StoryPage']


# class JournalPage(Page):
#     template = 'studio/journal.html'
#
#     parent_page_types = ['StudioPage']
#     subpage_types = []
#
#     def get_context(self, request, *args, **kwargs):
#         context = super().get_context(request, *args, **kwargs)
#         return context
#
#     def __str__(self):
#         return self.title


class InterviewPage(Page):
    template = 'studio/interview.html'

    parent_page_types = ['StudioPage']
    subpage_types = []

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        return context

    def __str__(self):
        return self.title


class StoryPage(Page):
    template = 'studio/story.html'

    parent_page_types = ['StudioPage']
    subpage_types = []

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        return context

    def __str__(self):
        return self.title
