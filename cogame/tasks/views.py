from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from status.utils import StatusFilterMixin
from tasks.models import Task

__author__ = 'eraldo'


class TaskMixin:
    model = Task
    fields = ['project', 'name', 'description', 'status', 'date', 'deadline', 'tags']


class TaskListView(StatusFilterMixin, TaskMixin, ListView):
    status_default = ['open']

    def get_queryset(self):
        queryset = super(TaskListView, self).get_queryset()
        return self.filter_status(queryset)


class TaskNewView(TaskMixin, CreateView):
    success_url = reverse_lazy('tasks:task_new')

    def get_initial(self):
        initial = super(TaskNewView, self).get_initial()
        project = self.request.GET.get('project')
        if project:
            initial['project'] = project
        return initial


class TaskShowView(TaskMixin, DetailView):
    template_name = "tasks/task_show.html"


class TaskEditView(TaskMixin, UpdateView):
    success_url = reverse_lazy('tasks:task_list')


class TaskDeleteView(TaskMixin, DeleteView):
    success_url = reverse_lazy('tasks:task_list')