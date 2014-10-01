from django.conf.urls import patterns, url
from dojo.views import DojoView, ModuleCreateView, ModuleShowView, ModuleEditView, ModuleDeleteView

__author__ = 'eraldo'

urlpatterns = patterns(
    '',
    # ex: ../
    url(r'^$',
        DojoView.as_view(),
        name='home'),
    # ex: ../new/
    url(r'^new/$',
        ModuleCreateView.as_view(),
        name='module_new'),
    # ex: ../4/
    url(r'^(?P<pk>\d+)/$',
        ModuleShowView.as_view(),
        name='module_show'),
    # ex: ../edit/
    url(r'^(?P<pk>\d+)/edit/$',
        ModuleEditView.as_view(),
        name='module_edit'),

    # ex: ../4/delete/
    url(r'^(?P<pk>\d+)/delete/$',
        ModuleDeleteView.as_view(),
        name='module_delete'),

)
