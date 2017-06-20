from dal_select2.views import Select2QuerySetView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, DeleteView, RedirectView
from rest_framework import viewsets

from colegend.core.views import OwnedCreateView, OwnedUpdateView, OwnedItemsMixin
from .models import Outcome
from .forms import OutcomeForm, OutcomeQuickCreateForm
from .filters import OutcomeFilter
from .serializers import OutcomeSerializer


class OutcomeViewSet(viewsets.ModelViewSet):
    queryset = Outcome.objects.all()
    serializer_class = OutcomeSerializer
    filter_fields = ['status', 'scope']

    def get_queryset(self):
        user = self.request.user
        return user.outcomes.all()


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
        self.filter = self.filter_class(data=self.request.GET, queryset=queryset)
        filter_data = dict(self.filter.data.items())
        if filter_data.get('inbox') == '1':
            filter_data.pop('inbox')
        self.filter.active = any([value for key, value in filter_data.items() if key not in  ['filter', 'page']])
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
        context['inbox'] = self.filter.data.get('inbox') == '2'
        return context


class OutcomeAgendaView(OutcomeListView):
    template_name = 'outcomes/agenda.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['quick_create_form'] = self.get_quick_create_form()
        context['agenda'] = True
        user = self.request.user
        # context['focus_outcomes'] =
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


class OutcomeInboxToggleView(OutcomeUpdateView):
    def post(self, request, *args, **kwargs):
        user = request.user
        outcome = self.get_object()
        if outcome.owned_by(user):
            outcome.inbox = not outcome.inbox
            outcome.save()
            return redirect(self.get_success_url())
        return super().post(request)


class OutcomeInboxView(RedirectView):
    pattern_name = 'outcomes:list'
    query_string = True

    def get_redirect_url(self, *args, **kwargs):
        url = super().get_redirect_url(*args, **kwargs)
        args = self.request.META.get('QUERY_STRING', '')
        return '{url}{prefix}{suffix}'.format(
            url=url,
            prefix='&' if args else '?',
            suffix='inbox=2',
        )


class OutcomeAutocompleteView(LoginRequiredMixin, OutcomeMixin, Select2QuerySetView):
    """
    A django view providing autocomplete data.
    """
    create_field = 'name'

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        return queryset.owned_by(user).open()

    def create_object(self, text):
        """Create an object given a text."""
        owner = self.request.user
        return self.get_queryset().create(**{self.create_field: text}, owner=owner)

    def has_add_permission(self, request):
        """Return True if the user has the permission to add a model."""
        if not request.user.is_authenticated():
            return False
        return True
