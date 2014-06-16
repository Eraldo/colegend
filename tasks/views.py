from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from tasks.models import Task

__author__ = 'eraldo'


class TaskListView(ListView):
    model = Task


class TaskCreateView(CreateView):
    model = Task
    success_url = reverse_lazy('tasks:list')


class TaskDetailView(DetailView):
    model = Task


class TaskUpdateView(UpdateView):
    model = Task
    success_url = reverse_lazy('tasks:list')


class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy('tasks:list')