from django.db import models
from django.shortcuts import redirect
from wagtail.core.models import Page
from django.utils.translation import ugettext_lazy as _

from colegend.core.fields import MarkdownField
from colegend.core.models import OwnedBase, TimeStampedBase, AutoOwnedBase
from colegend.scopes.models import SCOPE_CHOICES, DAY, get_scope_by_name


class InterviewEntry(OwnedBase, TimeStampedBase):
    """
    A django model representing a user's interview entry.
    """
    scope = models.CharField(
        _('scope'),
        choices=SCOPE_CHOICES,
        default=DAY,
        max_length=5,
    )
    start = models.DateField(
        _('start'),
    )

    likes = models.TextField()
    dislikes = models.TextField()

    # challenge = models.TextField(help_text=_('I had troubles with...'))
    # celebration = models.TextField(help_text=_('I enjoyed...'))
    # success = models.TextField(help_text=_('I am proud of...'))
    # connection = models.TextField(help_text=_('I had a great time with...'))
    # expression = models.TextField(help_text=_('I did not share...'))
    # learning = models.TextField(help_text=_('I learned that...'))
    # gratitude = models.TextField(help_text=_('I am thankful for...'))

    class Meta:
        verbose_name = _('Interview')
        verbose_name_plural = _('Interviews')
        unique_together = ['owner', 'scope', 'start']
        ordering = ['-start']
        get_latest_by = 'start'
        default_related_name = 'interview_entries'

    def __str__(self):
        return "{}'s {} interview entries {}".format(self.owner, self.get_scope_display(), self.start)

    def save(self, *args, **kwargs):
        if self.pk is None:  # Creation.
            # Adapting start date to scope.
            scope = get_scope_by_name(self.scope)(self.start)
            self.start = scope.start
        super().save(*args, **kwargs)


class Story(AutoOwnedBase):
    class Meta:
        verbose_name = _('Story')
        verbose_name_plural = _('Stories')
        default_related_name = 'story'

    def __str__(self):
        return "{}'s story".format(self.owner)


class Chapter(TimeStampedBase):
    story = models.ForeignKey(
        to=Story,
        on_delete=models.CASCADE,
    )
    name = models.CharField(
        _('name'),
        max_length=255,
        blank=True
    )
    content = MarkdownField()

    class Meta:
        verbose_name = _('Chapter')
        verbose_name_plural = _('Chapters')
        default_related_name = 'chapters'
        ordering = ['-created']

    def __str__(self):
        return "{}".format(self.name)


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
