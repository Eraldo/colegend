from annoying.functions import get_object_or_None
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from tutorials.forms import TutorialForm
from tutorials.models import Tutorial
from lib.views import ManagerRequiredMixin, ActiveUserRequiredMixin

__author__ = 'eraldo'


class TutorialMixin():
    model = Tutorial
    form_class = TutorialForm


class TutorialListView(ActiveUserRequiredMixin, TutorialMixin, ListView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tutorial'] = get_object_or_None(Tutorial, name="Tutorials")
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
