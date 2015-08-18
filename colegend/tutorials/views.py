from annoying.functions import get_object_or_None
from django.core.urlresolvers import reverse_lazy
from django.http import Http404
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView, RedirectView
from tutorials.forms import TutorialForm
from tutorials.models import Tutorial
from lib.views import ManagerRequiredMixin, ActiveUserRequiredMixin

__author__ = 'eraldo'


class TutorialMixin():
    model = Tutorial
    form_class = TutorialForm
    icon = "tutorial"
    tutorial = "Tutorials"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class TutorialListView(ActiveUserRequiredMixin, TutorialMixin, ListView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_counter'] = self.get_queryset().count()
        return context


class TutorialCreateView(ManagerRequiredMixin, TutorialMixin, CreateView):
    success_url = reverse_lazy('tutorials:tutorial_list')


class TutorialShowView(ActiveUserRequiredMixin, TutorialMixin, DetailView):
    template_name = "tutorials/tutorial_show.html"


class TutorialEditView(ManagerRequiredMixin, TutorialMixin, UpdateView):
    pass


class TutorialDeleteView(ManagerRequiredMixin, TutorialMixin, DeleteView):
    template_name = "confirm_delete.html"
    success_url = reverse_lazy('tutorials:tutorial_list')


class TutorialRedirectView(RedirectView):
    permanent = False
    name = None

    def get_redirect_url(self, *args, **kwargs):
        if not self.name:
            raise Http404
        try:
            return reverse_lazy("tutorials:tutorial_show",
                               args=[Tutorial.objects.get(name=self.name).pk])
        except Tutorial.DoesNotExist:
            raise Http404


class KeyboardTutorialView(DetailView):
    template_name = "tutorials/_tutorial.html"

    def get_object(self, queryset=None):
        return Tutorial.objects.get(name="Keyboard")
