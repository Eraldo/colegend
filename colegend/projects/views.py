from lib.views import ActiveUserRequiredMixin
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
        queryset = super(ProjectListView, self).get_queryset()
        return self.filter_status(queryset)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['counter'] = self.get_queryset().count()
        return context


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
    template_name = "confirm_delete.html"
    success_url = reverse_lazy('projects:project_list')
