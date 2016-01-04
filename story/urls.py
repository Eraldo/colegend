from django.conf.urls import patterns, url

from .views import Chapter1View, PrologueView, WelcomeTreeView, WelcomeTreeLeafWidgetView, \
    PioneerJournalView, YourJournalView, LeyendaView, StoryView

__author__ = 'eraldo'

urlpatterns = patterns(
    '',
    url(r'^$',
        StoryView.as_view(),
        name='index'),
    url(r'^chapter-1/$',
        Chapter1View.as_view(),
        name='chapter1'),
    url(r'^prologue/$',
        PrologueView.as_view(),
        name='prologue'),
    url(r'^welcome-tree/$',
        WelcomeTreeView.as_view(),
        name='welcome-tree'),
    url(r'^welcome-tree/leaf/$',
        WelcomeTreeLeafWidgetView.as_view(),
        name='tree-leaf'),
    url(r'^leyenda/$',
        LeyendaView.as_view(),
        name='leyenda'),
    url(r'^poineer-journal/$',
        PioneerJournalView.as_view(),
        name='poineer-journal'),
    url(r'^your-journal/$',
        YourJournalView.as_view(),
        name='your-journal'),
)
