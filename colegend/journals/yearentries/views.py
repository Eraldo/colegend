from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView, RedirectView

from colegend.core.views import OwnerRequiredMixin
from colegend.journals.models import JournalPage
from colegend.journals.quarterentries.models import QuarterEntry
from colegend.journals.scopes import Year
from .forms import YearEntryForm
from .models import YearEntry


class YearEntryMixin(object):
    """
    Default attributes and methods for yearentry related views.
    """
    model = YearEntry
    form_class = YearEntryForm

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


class YearEntryIndexView(RedirectView):
    permanent = False
    query_string = True
    pattern_name = 'yearentries:list'


class YearEntryListView(LoginRequiredMixin, YearEntryMixin, ListView):
    template_name = 'yearentries/list.html'
    context_object_name = 'yearentries'


class YearEntryCreateView(LoginRequiredMixin, YearEntryMixin, CreateView):
    template_name = 'yearentries/create.html'

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

        # Creation year/year is given or curreny year/year as default.
        scope = Year()
        year = self.request.GET.get('year', scope.number)
        initial['year'] = year

        # default content
        initial['content'] = journal.year_template

        # prefill tags
        quarters = QuarterEntry.objects.owned_by(user).filter(year=scope.number)
        if quarters:
            tags = quarters.values_list('tags', flat=True)
            initial['tags'] = set(tags)

        return initial


class YearEntryDetailView(LoginRequiredMixin, OwnerRequiredMixin, YearEntryMixin, DetailView):
    template_name = 'yearentries/detail.html'


class YearEntryUpdateView(LoginRequiredMixin, OwnerRequiredMixin, YearEntryMixin, UpdateView):
    template_name = 'yearentries/update.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['journal'] = self.request.user.journal
        return kwargs


class YearEntryDeleteView(LoginRequiredMixin, OwnerRequiredMixin, YearEntryMixin, DeleteView):
    template_name = 'yearentries/delete.html'

    def get_success_url(self):
        yearentry = self.get_object()
        return yearentry.journal.index_url
