from django.conf.urls import patterns, url
from .views import Chapter1View, PrologueView, WelcomeTreeView, WelcomeTreeLeafWidgetView

__author__ = 'eraldo'

urlpatterns = patterns(
    '',
    url(r'^chapter-1$',
        Chapter1View.as_view(),
        name='chapter1'),
    url(r'^prologue$',
        PrologueView.as_view(),
        name='prologue'),
    url(r'^welcome-tree$',
        WelcomeTreeView.as_view(),
        name='welcome-tree'),
    url(r'^welcome-tree/leaf$',
        WelcomeTreeLeafWidgetView.as_view(),
        name='tree-leaf'),
)
