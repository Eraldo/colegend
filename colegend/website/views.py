from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView
from features.models import Feature
from habits.models import Habit
from lib.views import ActiveUserRequiredMixin
from news.models import NewsBlock
from quotes.models import Quote
from routines.models import Routine
from statuses.models import Status
from tasks.models import Task

__author__ = 'eraldo'


class AboutView(TemplateView):
    template_name = "website/about.html"

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context['feature'] = Feature.objects.first()
        return context


class HomeView(ActiveUserRequiredMixin, TemplateView):
    template_name = "website/home.html"
    login_url = reverse_lazy('about')
    icon = "home"
    tutorial = "Home"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        quote = Quote.objects.daily_quote()
        context['quote'] = quote
        number_of_newsblocks = 1
        context['newsblocks'] = NewsBlock.objects.filter(sticky=False)[0:number_of_newsblocks]
        context['sticky_newsblocks'] = NewsBlock.objects.filter(sticky=True)[0:number_of_newsblocks]
        return context


class SearchView(ActiveUserRequiredMixin, TemplateView):
    template_name = 'website/search.html'
    icon = "search"
    tutorial = "Search"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        query = self.request.GET.get("q")
        if query:
            user = self.request.user
            context["projects"] = user.projects.filter(name__icontains=query)
            context["tasks"] = user.tasks.filter(name__icontains=query)
            context["routines"] = Routine.objects.owned_by(user).filter(name__icontains=query)
            context["habits"] = Habit.objects.owned_by(user).filter(name__icontains=query)
            context["tags"] = user.tags.filter(name__icontains=query)
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


class ChatView(ActiveUserRequiredMixin, TemplateView):
    icon = "chat"
    template_name = "website/chat.html"

    def get(self, request, *args, **kwargs):
        message = "Info: The chat needs quite some time to load."
        messages.add_message(self.request, messages.INFO, message)
        return super().get(self.request, *args, **kwargs)


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
