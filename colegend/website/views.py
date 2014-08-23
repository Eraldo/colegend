import datetime
from braces.views import LoginRequiredMixin
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse_lazy
from django.utils.timesince import timeuntil
from django.views.generic import TemplateView
from features.models import Feature
from habits.models import Habit
from projects.models import Project
from routines.models import Routine
from statuses.models import Status
from tags.models import Tag
from tasks.models import Task

__author__ = 'eraldo'


class AboutView(TemplateView):
    template_name = "website/about.html"

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context['feature'] = Feature.objects.first()
        return context


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "website/home.html"

    login_url = reverse_lazy('about')


class CoSpaceView(LoginRequiredMixin, TemplateView):
    template_name = "website/cospace.html"

    def get_counter(self):
        now = datetime.datetime.now()
        date = datetime.datetime(now.year, now.month, now.day, 16, 4)
        while date.weekday() != 6:
            date += datetime.timedelta(1)
        return timeuntil(date, now)

    def get_context_data(self, **kwargs):
        context = super(CoSpaceView, self).get_context_data(**kwargs)
        context['counter'] = self.get_counter()
        return context


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
