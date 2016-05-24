from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView, RedirectView

from colegend.core.views import OwnedCreateView, OwnedUpdateView, OwnedItemsMixin
from .models import Outcome
from .forms import OutcomeForm


class OutcomeMixin(OwnedItemsMixin):
    """
    Default attributes and methods for outcome related views.
    """
    model = Outcome
    form_class = OutcomeForm


class OutcomeIndexView(RedirectView):
    permanent = False
    query_string = True
    pattern_name = 'outcomes:list'


class OutcomeListView(LoginRequiredMixin, OutcomeMixin, ListView):
    template_name = 'outcomes/list.html'
    context_object_name = 'outcomes'


class OutcomeCreateView(LoginRequiredMixin, OutcomeMixin, OwnedCreateView):
    template_name = 'outcomes/create.html'


class OutcomeDetailView(LoginRequiredMixin, OutcomeMixin, DetailView):
    template_name = 'outcomes/detail.html'


class OutcomeUpdateView(LoginRequiredMixin, OutcomeMixin, OwnedUpdateView):
    template_name = 'outcomes/update.html'


class OutcomeDeleteView(LoginRequiredMixin, OutcomeMixin, DeleteView):
    template_name = 'outcomes/delete.html'

    def get_success_url(self):
        outcome = self.get_object()
        return outcome.index_url
