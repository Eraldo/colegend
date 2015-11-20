from django.conf.urls import patterns, url

from .views import Chapter1View, PrologueView, PoetreeView

__author__ = 'eraldo'


urlpatterns = patterns(
    '',
    url(r'^chapter-1$',
        Chapter1View.as_view(),
        name='chapter1'),
    url(r'^poetree$',
        PoetreeView.as_view(),
        name='poetree'),
    url(r'^prologue$',
        PrologueView.as_view(),
        name='prologue'),
)
