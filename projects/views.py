from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from projects.models import Project

__author__ = 'eraldo'


class ProjectListView(ListView):
    model = Project


class ProjectCreateView(CreateView):
    model = Project
    success_url = reverse_lazy('projects:list')


class ProjectDetailView(DetailView):
    model = Project


class ProjectUpdateView(UpdateView):
    model = Project
    success_url = reverse_lazy('projects:list')


class ProjectDeleteView(DeleteView):
    model = Project
    success_url = reverse_lazy('projects:list')