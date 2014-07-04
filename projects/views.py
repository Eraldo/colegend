from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from projects.models import Project

__author__ = 'eraldo'


class ProjectBaseView:
    model = Project
    fields = ['name', 'description', 'status', 'deadline', 'tags']


class ProjectListView(ProjectBaseView, ListView):
    pass


class ProjectNewView(ProjectBaseView, CreateView):
    success_url = reverse_lazy('projects:project_list')


class ProjectShowView(ProjectBaseView, DetailView):
    template_name = "projects/project_show.html"


class ProjectEditView(ProjectBaseView, UpdateView):
    success_url = reverse_lazy('projects:project_list')


class ProjectDeleteView(ProjectBaseView, DeleteView):
    success_url = reverse_lazy('projects:project_list')