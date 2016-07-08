from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView, RedirectView
from django.views.generic.edit import FormMixin

from colegend.core.views import OwnedCreateView, OwnedUpdateView, OwnedItemsMixin
from .models import Outcome
from .forms import OutcomeForm, OutcomeQuickCreateForm
from .filters import OutcomeFilter


class OutcomeMixin(OwnedItemsMixin):
    """
    Default attributes and methods for outcome related views.
    """
    model = Outcome
    form_class = OutcomeForm
    filter_class = OutcomeFilter


class OutcomeIndexView(RedirectView):
    permanent = False
    query_string = True
    pattern_name = 'outcomes:list'


class OutcomeListView(LoginRequiredMixin, OutcomeMixin, ListView):
    template_name = 'outcomes/list.html'
    context_object_name = 'outcomes'
    context_filter_name = 'filter'
    filter_class = OutcomeFilter
    filter = None
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()

        request = self.request
        self.filter = self.filter_class(data=request.GET, queryset=queryset)

        return self.filter.qs

    def get_quick_create_form(self):
        kwargs = {
            'initial': {'owner': self.request.user},
            'next': self.request.path,
        }
        if self.request.method in ('POST', 'PUT'):
            kwargs.update({
                'data': self.request.POST,
            })
        return OutcomeQuickCreateForm(**kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[self.context_filter_name] = self.filter
        context['quick_create_form'] = self.get_quick_create_form()
        return context


class OutcomeCreateView(LoginRequiredMixin, OutcomeMixin, OwnedCreateView):
    template_name = 'outcomes/create.html'

    def get_success_url(self):
        request = self.request
        next_url = request.POST.get('next', request.GET.get('next'))
        if next_url:
            return next_url
        return super().get_success_url()


class OutcomeDetailView(LoginRequiredMixin, OutcomeMixin, DetailView):
    template_name = 'outcomes/detail.html'


class OutcomeUpdateView(LoginRequiredMixin, OutcomeMixin, OwnedUpdateView):
    template_name = 'outcomes/update.html'

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return super().get_success_url()


class OutcomeDeleteView(LoginRequiredMixin, OutcomeMixin, DeleteView):
    template_name = 'outcomes/delete.html'

    def get_success_url(self):
        outcome = self.get_object()
        return outcome.index_url
