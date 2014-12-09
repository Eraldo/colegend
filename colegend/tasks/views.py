from django.shortcuts import redirect
from lib.views import ActiveUserRequiredMixin
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from lib.views import OwnedItemsMixin
from statuses.utils import StatusFilterMixin
from tasks.forms import TaskForm
from tasks.models import Task

__author__ = 'eraldo'


class TaskMixin(ActiveUserRequiredMixin, OwnedItemsMixin):
    model = Task
    form_class = TaskForm
    icon = "task"
    tutorial = "Tasks"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_form(self, form_class):
        form = super(TaskMixin, self).get_form(form_class)
        # limit project choices to owned projects
        projects = form.fields['project'].queryset
        form.fields['project'].queryset = projects.owned_by(self.request.user)
        # limit tag choices to owned tags
        tags = form.fields['tags'].queryset
        form.fields['tags'].queryset = tags.owned_by(self.request.user)
        return form

    def form_valid(self, form):
        try:
            return super(TaskMixin, self).form_valid(form)
        except ValidationError as e:
            # Catch model errors (e.g. unique_together).
            form.add_error(None, e)
            return super(TaskMixin, self).form_invalid(form)


class TaskListView(StatusFilterMixin, TaskMixin, ListView):
    def get_queryset(self):
        queryset = super(TaskListView, self).get_queryset()
        return self.filter_status(queryset)


class TaskNewView(TaskMixin, CreateView):
    success_url = reverse_lazy('tasks:task_list')

    def get_initial(self):
        initial = super(TaskNewView, self).get_initial()
        project = self.request.GET.get('project')
        if project:
            initial['project'] = project
        return initial

    def form_valid(self, form):
        user = self.request.user
        form.instance.owner = user
        return super(TaskNewView, self).form_valid(form)


class TaskShowView(TaskMixin, DetailView):
    template_name = "tasks/task_show.html"


class TaskEditView(TaskMixin, UpdateView):
    success_url = reverse_lazy('tasks:task_list')


class TaskDeleteView(TaskMixin, DeleteView):
    template_name = "confirm_delete.html"
    success_url = reverse_lazy('tasks:task_list')


def task_complete(request, pk):
    task = Task.objects.get(pk=pk, owner=request.user)
    task.complete()

    next_url = request.POST.get('next')
    if next_url:
        return redirect(next)
    return redirect(task)

