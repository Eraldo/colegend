from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from tasks.models import Task

__author__ = 'eraldo'


class TaskBaseView:
    model = Task
    fields = ['project', 'name', 'description', 'status', 'date', 'deadline', 'tags']


class TaskListView(TaskBaseView, ListView):
    status_default = ['open']

    def get_queryset(self):
        queryset = super(TaskListView, self).get_queryset()

        # filter by status
        status_list = self.request.GET.getlist('status', self.status_default)
        for status in status_list:
            queryset = queryset.status(status)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(TaskListView, self).get_context_data(**kwargs)

        # handle status (open|closed)
        state = self.request.GET.get('state', self.status_default)
        context['state'] = state

        return context


class TaskNewView(TaskBaseView, CreateView):
    success_url = reverse_lazy('tasks:task_new')

    def get_initial(self):
        initial = super(TaskNewView, self).get_initial()
        project = self.request.GET.get('project')
        if project:
            initial['project'] = project
        return initial


class TaskShowView(TaskBaseView, DetailView):
    template_name = "tasks/task_show.html"


class TaskEditView(TaskBaseView, UpdateView):
    success_url = reverse_lazy('tasks:task_list')


class TaskDeleteView(TaskBaseView, DeleteView):
    success_url = reverse_lazy('tasks:task_list')