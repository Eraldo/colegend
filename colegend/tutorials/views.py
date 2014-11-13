from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from tutorials.forms import TutorialForm
from tutorials.models import Tutorial
from lib.views import ManagerRequiredMixin

__author__ = 'eraldo'


class TutorialMixin(ManagerRequiredMixin):
    model = Tutorial
    form_class = TutorialForm


class TutorialListView(TutorialMixin, ListView):
    pass


class TutorialCreateView(TutorialMixin, CreateView):
    success_url = reverse_lazy('tutorials:tutorial_list')


class TutorialShowView(TutorialMixin, DetailView):
    template_name = "tutorials/tutorial_show.html"


class TutorialEditView(TutorialMixin, UpdateView):
    pass


class TutorialDeleteView(TutorialMixin, DeleteView):
    success_url = reverse_lazy('tutorials:tutorial_list')
