from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from projects.models import Project
from status.utils import StatusFilterMixin

__author__ = 'eraldo'


class ProjectMixin:
    model = Project
    fields = ['name', 'description', 'status', 'deadline', 'tags']


class ProjectListView(StatusFilterMixin, ProjectMixin, ListView):
    def get_queryset(self):
        queryset = super(ProjectListView, self).get_queryset()
        return self.filter_status(queryset)


class ProjectNewView(ProjectMixin, CreateView):
    success_url = reverse_lazy('projects:project_list')


class ProjectShowView(StatusFilterMixin, ProjectMixin, DetailView):
    template_name = "projects/project_show.html"

    def get_context_data(self, **kwargs):
        context = super(ProjectShowView, self).get_context_data(**kwargs)
        project = self.get_object()
        tasks = project.tasks.all()
        context["tasks"] = self.filter_status(tasks)
        return context


class ProjectEditView(ProjectMixin, UpdateView):
    success_url = reverse_lazy('projects:project_list')


class ProjectDeleteView(ProjectMixin, DeleteView):
    success_url = reverse_lazy('projects:project_list')