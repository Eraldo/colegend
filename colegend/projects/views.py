from django.contrib import messages
from django.http import HttpResponseForbidden
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from lib.views import ActiveUserRequiredMixin, get_sound
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from lib.views import OwnedItemsMixin
from projects.forms import ProjectForm
from projects.models import Project
from statuses.utils import StatusFilterMixin

__author__ = 'eraldo'


class ProjectMixin(ActiveUserRequiredMixin, OwnedItemsMixin):
    model = Project
    form_class = ProjectForm
    icon = "project"
    tutorial = "Projects"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_form(self, form_class):
        form = super(ProjectMixin, self).get_form(form_class)
        # Limit tag choices to owned tags.
        tags = form.fields['tags'].queryset
        form.fields['tags'].queryset = tags.owned_by(self.request.user)
        return form

    def form_valid(self, form):
        try:
            return super(ProjectMixin, self).form_valid(form)
        except ValidationError as e:
            # Catch model errors (e.g. unique_together).
            form.add_error(None, e)
            return super(ProjectMixin, self).form_invalid(form)


class ProjectListView(StatusFilterMixin, ProjectMixin, ListView):
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        return self.filter_status(queryset)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_counter'] = self.get_queryset().count()
        context['next_counter'] = self.request.user.projects.next().count()
        return context


class ProjectNewView(ProjectMixin, CreateView):
    def form_valid(self, form):
        # Check if the hidden owner was changed. (security check)
        if form.cleaned_data["owner"] != self.request.user:
            return HttpResponseForbidden()
        response = super().form_valid(form)
        project = self.object
        if project:
            message = "Created Project: {project}.".format(
                project=render_to_string("projects/_project_link.html", {"project": project})
            )
            messages.add_message(self.request, messages.SUCCESS, mark_safe(message))
        return response

    def get_initial(self):
        initial = super().get_initial()
        initial.update({"owner": self.request.user})
        return initial


class ProjectShowView(StatusFilterMixin, ProjectMixin, DetailView):
    template_name = "projects/project_show.html"

    def get_context_data(self, **kwargs):
        context = super(ProjectShowView, self).get_context_data(**kwargs)
        project = self.get_object()
        tasks = project.tasks.all()
        context["tasks"] = self.filter_status(tasks)
        return context


class ProjectEditView(ProjectMixin, UpdateView):
    def form_valid(self, form):
        if "status" in form.changed_data:
            if form.instance.old_status.open() and form.instance.status.closed():
                add_project_success_message(self.request, form.instance)
        return super().form_valid(form)


class ProjectDeleteView(ProjectMixin, DeleteView):
    template_name = "confirm_delete.html"
    success_url = reverse_lazy('projects:project_list')


def add_project_success_message(request, project):
    message = """{status} Project: {project}.""".format(
        status=str(project.status).capitalize(),
        project=render_to_string("projects/_project_link.html", {"project": project})
    )
    if request.user.settings.sound:
        sound = get_sound("project-success")
        if sound:
            message += sound
    messages.add_message(request, messages.SUCCESS, mark_safe(message))
