from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView, RedirectView

from colegend.core.views import OwnerRequiredMixin
from colegend.journals.models import JournalPage
from .forms import DayEntryForm
from .models import DayEntry


class DayEntryMixin(object):
    """
    Default attributes and methods for dayentry related views.
    """
    model = DayEntry
    form_class = DayEntryForm

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


class DayEntryIndexView(RedirectView):
    permanent = False
    query_string = True
    pattern_name = 'dayentries:list'


class DayEntryListView(LoginRequiredMixin, DayEntryMixin, ListView):
    template_name = 'dayentries/list.html'
    context_object_name = 'dayentries'


class DayEntryCreateView(LoginRequiredMixin, DayEntryMixin, CreateView):
    template_name = 'dayentries/create.html'

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


        # Creation date is given or today as default.
        date = self.request.GET.get('date', timezone.now().date())
        initial['date'] = date

        # default content
        initial['content'] = journal.day_template

        # default focus
        initial['focus'] = journal.focus_template

        # Prefill the entry based on the previous entry if found.
        previous = DayEntry.objects.owned_by(user).filter(date__lte=date).first()
        if previous:
            initial['locations'] = previous.locations
            initial['tags'] = previous.tags.all()

        return initial


class DayEntryDetailView(LoginRequiredMixin, OwnerRequiredMixin, DayEntryMixin, DetailView):
    template_name = 'dayentries/detail.html'


class DayEntryUpdateView(LoginRequiredMixin, OwnerRequiredMixin, DayEntryMixin, UpdateView):
    template_name = 'dayentries/update.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['journal'] = self.request.user.journal
        return kwargs


class DayEntryDeleteView(LoginRequiredMixin, OwnerRequiredMixin, DayEntryMixin, DeleteView):
    template_name = 'dayentries/delete.html'

    def get_success_url(self):
        dayentry = self.get_object()
        return dayentry.journal.index_url
