from django.conf.urls import patterns, url
from commands.views import quick_command

__author__ = 'eraldo'

urlpatterns = patterns(
    '',
    ## Actions

    # ex: ../quick/
    url(r'^$',
        quick_command,
        name='quick_command'),
)
