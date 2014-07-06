from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from tasks.models import Task

__author__ = 'eraldo'


class TaskBaseView:
    model = Task
    fields = ['project', 'name', 'description', 'status', 'date', 'deadline', 'tags']


class TaskListView(TaskBaseView, ListView):
    status_default = ['open']

    def filter_status(self, queryset):
        """
        Filter querysey by posted status

        :param queryset:
        :return:
        """
        status_list = self.request.GET.getlist('status', self.status_default)
        for status in status_list:
            queryset = queryset.status(status)
        return queryset

    def add_status_to_context(self, context):
        """
        Add the posted status to the context dictionary

        :param context: context dictionary
        """
        status = self.request.GET.getlist('status', self.status_default)
        context['status'] = status

    def get_queryset(self):
        queryset = super(TaskListView, self).get_queryset()
        return self.filter_status(queryset)

    def get_context_data(self, **kwargs):
        context = super(TaskListView, self).get_context_data(**kwargs)
        self.add_status_to_context(context)
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