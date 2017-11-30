from django.core.validators import MaxValueValidator
from django.db import models
from django.shortcuts import redirect
from wagtail.wagtailcore.models import Page

from colegend.core.fields import MarkdownField
from colegend.core.models import TimeStampedBase, OwnedBase
from django.utils.translation import ugettext_lazy as _


class Book(TimeStampedBase):
    name = models.CharField(
        _('name'),
        max_length=255,
        unique=True
    )
    author = models.CharField(
        _('author'),
        max_length=255,
    )
    image_url = models.URLField(
        _('image url'),
        blank=True
    )
    url = models.URLField(
        _('url'),
        blank=True
    )
    content = MarkdownField(
        blank=True
    )
    featured = models.BooleanField(
        default=False
    )

    class Meta:
        default_related_name = 'books'
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Making sure only one book can be featured.

        if self.featured:
            try:
                temp = Book.objects.get(featured=True)
                if self != temp:
                    temp.featured = False
                    temp.save()
            except Book.DoesNotExist:
                pass
        return super().save(*args, **kwargs)


class BookReview(OwnedBase, TimeStampedBase):
    book = models.ForeignKey(
        to=Book,
        on_delete=models.CASCADE
    )
    rating = models.PositiveSmallIntegerField(
        _('rating'),
    )
    area_1 = models.PositiveSmallIntegerField(
        _('area 1'),
        validators=[MaxValueValidator(100)]
    )
    area_2 = models.PositiveSmallIntegerField(
        _('area 2'),
        validators=[MaxValueValidator(100)]
    )
    area_3 = models.PositiveSmallIntegerField(
        _('area 3'),
        validators=[MaxValueValidator(100)]
    )
    area_4 = models.PositiveSmallIntegerField(
        _('area 4'),
        validators=[MaxValueValidator(100)]
    )
    area_5 = models.PositiveSmallIntegerField(
        _('area 5'),
        validators=[MaxValueValidator(100)]
    )
    area_6 = models.PositiveSmallIntegerField(
        _('area 6'),
        validators=[MaxValueValidator(100)]
    )
    area_7 = models.PositiveSmallIntegerField(
        _('area 7'),
        validators=[MaxValueValidator(100)]
    )
    content = MarkdownField()

    class Meta:
        default_related_name = 'book_reviews'
        unique_together = ['owner', 'book']

    def __str__(self):
        return 'Book review'


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
