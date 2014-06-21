from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from projects.models import Project

__author__ = 'eraldo'


class ProjectListView(ListView):
    model = Project


class ProjectNewView(CreateView):
    model = Project
    success_url = reverse_lazy('projects:project_list')


class ProjectShowView(DetailView):
    model = Project
    template_name = "projects/project_show.html"


class ProjectEditView(UpdateView):
    model = Project
    success_url = reverse_lazy('projects:project_list')


class ProjectDeleteView(DeleteView):
    model = Project
    success_url = reverse_lazy('projects:project_list')