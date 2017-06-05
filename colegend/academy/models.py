from django.shortcuts import redirect
from wagtail.wagtailcore.models import Page


class AcademyPage(Page):
    template = 'academy/base.html'

    def serve(self, request, *args, **kwargs):
        return redirect(self.get_first_child().url)

    parent_page_types = ['cms.RootPage']
    subpage_types = ['CoursesPage', 'BookClubPage', 'QuizzesPage', 'resources.ResourcesPage']


class CoursesPage(Page):
    template = 'academy/courses.html'

    parent_page_types = ['AcademyPage']
    subpage_types = []

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        return context

    def __str__(self):
        return self.title


class BookClubPage(Page):
    template = 'academy/book_club.html'

    parent_page_types = ['AcademyPage']
    subpage_types = []

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        return context

    def __str__(self):
        return self.title


class QuizzesPage(Page):
    template = 'academy/quizzes.html'

    parent_page_types = ['AcademyPage']
    subpage_types = []

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        return context

    def __str__(self):
        return self.title


# class ResourcesPage(Page):
#     template = 'academy/resources.html'
#
#     parent_page_types = ['AcademyPage']
#     subpage_types = []
#
#     def get_context(self, request, *args, **kwargs):
#         context = super().get_context(request, *args, **kwargs)
#         return context
#
#     def __str__(self):
#         return self.title
