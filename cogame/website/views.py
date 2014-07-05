from django.contrib import messages
from django.views.generic import TemplateView
from projects.models import Project
from tags.models import Tag
from tasks.models import Task

__author__ = 'eraldo'


class TestView(TemplateView):
    template_name = "website/test.html"

    def get(self, request, *args, **kwargs):
        message = "test1"
        messages.add_message(request, messages.INFO, message)
        message = "test2"
        messages.add_message(request, messages.INFO, message)
        return super(TestView, self).get(request, *args, **kwargs)


class SearchView(TemplateView):
    template_name = 'website/search.html'

    def get_context_data(self, *args, **kwargs):
        context = super(SearchView, self).get_context_data(*args, **kwargs)
        q = self.request.GET.get("q")
        if q:
            context["projects"] = Project.objects.filter(name__icontains=q)
            context["tasks"] = Task.objects.filter(name__icontains=q)
            context["tags"] = Tag.objects.filter(name__icontains=q)
        return context