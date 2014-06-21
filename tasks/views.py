from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from tasks.models import Task

__author__ = 'eraldo'


class TaskListView(ListView):
    model = Task


class TaskNewView(CreateView):
    model = Task
    success_url = reverse_lazy('tasks:task_new')


class TaskShowView(DetailView):
    model = Task
    template_name = "tasks/task_show.html"


class TaskEditView(UpdateView):
    model = Task
    success_url = reverse_lazy('tasks:task_list')


class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy('tasks:task_list')