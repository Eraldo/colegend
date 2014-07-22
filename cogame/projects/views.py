from braces.views import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from lib.views import OwnedItemsMixin
from projects.models import Project
from statuses.utils import StatusFilterMixin

__author__ = 'eraldo'


class ProjectMixin(LoginRequiredMixin, OwnedItemsMixin):
    model = Project
    fields = ['name', 'description', 'status', 'deadline', 'tags']


class ProjectListView(StatusFilterMixin, ProjectMixin, ListView):
    def get_queryset(self):
        queryset = super(ProjectListView, self).get_queryset()
        return self.filter_status(queryset)


class ProjectNewView(ProjectMixin, CreateView):
    success_url = reverse_lazy('projects:project_list')

    def form_valid(self, form):
        user = self.request.user
        form.instance.owner = user
        return super(ProjectNewView, self).form_valid(form)


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
