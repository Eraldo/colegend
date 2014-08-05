from braces.views import LoginRequiredMixin
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.views.generic import TemplateView
from habits.models import Habit
from projects.models import Project
from routines.models import Routine
from statuses.models import Status
from tags.models import Tag
from tasks.models import Task

__author__ = 'eraldo'


class TestView(TemplateView):
    template_name = "website/test.html"

    def get(self, request, *args, **kwargs):
        # check permission
        if not request.user.is_superuser:
            raise PermissionDenied

        message = "test1"
        messages.add_message(request, messages.INFO, message)
        message = "test2"
        messages.add_message(request, messages.INFO, message)
        return super(TestView, self).get(request, *args, **kwargs)


class SearchResultsView(LoginRequiredMixin, TemplateView):
    template_name = 'website/search.html'

    def get_context_data(self, *args, **kwargs):
        context = super(SearchResultsView, self).get_context_data(*args, **kwargs)
        query = self.request.GET.get("q")
        if query:
            context["projects"] = Project.objects.filter(name__icontains=query)
            context["tasks"] = Task.objects.filter(name__icontains=query)
            context["routines"] = Routine.objects.filter(name__icontains=query)
            context["habits"] = Habit.objects.filter(name__icontains=query)
            context["tags"] = Tag.objects.filter(name__icontains=query)
        context["status_options"] = Status.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        name = request.POST.get("name")
        model = request.POST.get("model")
        if model and name:
            if model == "task":
                Task.objects.create(name=name)
            message = "todo: create {}:{}".format(model, name)
            messages.add_message(request, messages.INFO, message)
        return self.get(request, *args, **kwargs)
