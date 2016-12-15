from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView, RedirectView

from colegend.core.views import OwnerRequiredMixin
from colegend.journals.models import JournalPage
from colegend.journals.monthentries.models import MonthEntry
from colegend.journals.scopes import Quarter
from .forms import QuarterEntryForm
from .models import QuarterEntry


class QuarterEntryMixin(object):
    """
    Default attributes and methods for quarterentry related views.
    """
    model = QuarterEntry
    form_class = QuarterEntryForm

    def get_form(self):
        form = super().get_form()
        # limit tag choices to owned tags
        user = self.request.user
        form.fields['tags'].queryset = user.tags.all()
        return form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = JournalPage.objects.first()
        return context


class QuarterEntryIndexView(RedirectView):
    permanent = False
    query_string = True
    pattern_name = 'quarterentries:list'


class QuarterEntryListView(LoginRequiredMixin, QuarterEntryMixin, ListView):
    template_name = 'quarterentries/list.html'
    context_object_name = 'quarterentries'


class QuarterEntryCreateView(LoginRequiredMixin, QuarterEntryMixin, CreateView):
    template_name = 'quarterentries/create.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['journal'] = self.request.user.journal
        return kwargs

    def get_initial(self):
        initial = super().get_initial()

        # Set the default owned journal.
        user = self.request.user
        journal = user.journal
        initial['journal'] = journal

        # Creation year/quarter is given or curreny year/quarter as default.
        scope = Quarter()
        year = self.request.GET.get('year', scope.date.year)
        initial['year'] = year
        quarter = self.request.GET.get('quarter', scope.number)
        initial['quarter'] = quarter

        # default content
        initial['content'] = journal.quarter_template

        # prefill tags
        months = MonthEntry.objects.owned_by(user).filter(year=scope.date.year, month=scope.date.month)
        if months:
            tags = months.values_list('tags', flat=True)
            initial['tags'] = set(tags)

        return initial


class QuarterEntryDetailView(LoginRequiredMixin, OwnerRequiredMixin, QuarterEntryMixin, DetailView):
    template_name = 'quarterentries/detail.html'


class QuarterEntryUpdateView(LoginRequiredMixin, OwnerRequiredMixin, QuarterEntryMixin, UpdateView):
    template_name = 'quarterentries/update.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['journal'] = self.request.user.journal
        return kwargs


class QuarterEntryDeleteView(LoginRequiredMixin, OwnerRequiredMixin, QuarterEntryMixin, DeleteView):
    template_name = 'quarterentries/delete.html'

    def get_success_url(self):
        quarterentry = self.get_object()
        return quarterentry.journal.index_url
