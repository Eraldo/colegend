from annoying.functions import get_object_or_None
from django.contrib import messages
from django.http import HttpResponseForbidden
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.utils.html import escape
from django.utils.safestring import mark_safe
from lib.views import ActiveUserRequiredMixin, get_sound
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from lib.views import OwnedItemsMixin
from projects.models import Project
from statuses.utils import StatusFilterMixin
from tasks.forms import TaskForm
from tasks.models import Task

__author__ = 'eraldo'


class TaskMixin(ActiveUserRequiredMixin, OwnedItemsMixin):
    model = Task
    form_class = TaskForm
    icon = "task"
    tutorial = "Tasks"

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
    paginate_by = 10

    def get_queryset(self):
        queryset = super(TaskListView, self).get_queryset()
        return self.filter_status(queryset)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_counter'] = self.get_queryset().count()
        context['next_counter'] = self.request.user.tasks.next().filter(project__isnull=True).count()
        return context


class TaskNewView(TaskMixin, CreateView):
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return super().get_success_url()

    def get_initial(self):
        initial = super(TaskNewView, self).get_initial()
        initial.update({"owner": self.request.user})
        try:
            project_pk = int(self.request.GET.get('project'))
        except TypeError:
            project_pk = None
        if project_pk:
            project = get_object_or_None(Project, pk=project_pk, owner=self.request.user)
            if project:
                initial['project'] = project.pk
                # Use the projects tags as the default tags for the new task.
                initial['tags'] = project.tags.all()
        return initial

    def form_valid(self, form):
        # Check if the hidden owner was changed. (security check)
        if form.cleaned_data["owner"] != self.request.user:
            return HttpResponseForbidden()
        response = super().form_valid(form)
        task = self.object
        if task:
            message = """Created Task: {task}.""".format(
                task=render_to_string("tasks/_task_link.html", {"task": task})
            )
            messages.add_message(self.request, messages.SUCCESS, mark_safe(message))
        return response


class TaskShowView(TaskMixin, DetailView):
    template_name = "tasks/task_show.html"


class TaskEditView(TaskMixin, UpdateView):
    def form_valid(self, form):
        if "status" in form.changed_data:
            if form.instance.old_status.open() and form.instance.status.closed():
                add_task_success_message(self.request, form.instance)
        return super().form_valid(form)


class TaskDeleteView(TaskMixin, DeleteView):
    template_name = "confirm_delete.html"
    success_url = reverse_lazy('tasks:task_list')


def task_complete(request, pk):
    # prepare
    task = Task.objects.get(pk=pk, owner=request.user)
    # act
    completed = task.complete()
    if completed:
        add_task_success_message(request, task)
    # redirect
    next_url = request.POST.get('next')
    if next_url:
        return redirect(next_url)
    return redirect(task)


def add_task_success_message(request, task):
    message = """{status} Task: {task}.""".format(
        status=str(task.status).capitalize(),
        task=render_to_string("tasks/_task_link.html", {"task": task})
    )
    if request.user.settings.sound:
        sound = get_sound("task-success")
        if sound:
            message += sound
    messages.add_message(request, messages.SUCCESS, mark_safe(message))
