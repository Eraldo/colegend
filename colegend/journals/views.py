from django.core.urlresolvers import reverse
from django.utils import timezone
from lib.views import ActiveUserRequiredMixin
from django.core.exceptions import ValidationError
from django.views.generic import DetailView, UpdateView, DeleteView, CreateView, ArchiveIndexView, RedirectView
from journals.forms import DayEntryForm
from journals.models import DayEntry

__author__ = 'eraldo'


class DayEntryMixin(ActiveUserRequiredMixin):
    model = DayEntry
    form_class = DayEntryForm
    icon = "journal"
    tutorial = "Journal"

    def get_queryset(self):
        return super().get_queryset().owned_by(self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        try:
            return super(DayEntryMixin, self).form_valid(form)
        except ValidationError as e:
            # Catch model errors (e.g. unique_together).
            form.add_error(None, e)
            return super(DayEntryMixin, self).form_invalid(form)


class DayEntryListView(DayEntryMixin, ArchiveIndexView):
    date_field = "date"
    template_name = "journals/dayentry_list.html"
    allow_empty = True
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(DayEntryListView, self).get_context_data(**kwargs)
        context['counter'] = self.get_queryset().count()
        context['streak'] = DayEntry.objects.streak_for(self.request.user)
        return context


class DayEntryNewView(DayEntryMixin, CreateView):
    def form_valid(self, form):
        user = self.request.user
        form.instance.journal = user.journal
        return super(DayEntryNewView, self).form_valid(form)

    def get_initial(self):
        initial = super(DayEntryNewView, self).get_initial()
        user = self.request.user
        # template
        entry_template = user.settings.journal_entry_template
        if entry_template:
            initial['content'] = entry_template
        # location
        entry = DayEntry.objects.latest_for(user)
        if entry:
            initial['location'] = entry.location
        return initial


class DayEntryShowView(DayEntryMixin, DetailView):
    template_name = "journals/dayentry_show.html"


class DayEntryEditView(DayEntryMixin, UpdateView):
    pass


class DayEntryDeleteView(DayEntryMixin, DeleteView):
    template_name = "confirm_delete.html"


class DayEntryContinueView(DayEntryMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        user = self.request.user
        current_entry = user.journal.entries.filter(date=timezone.now().date()).first()
        if current_entry:
            return current_entry.get_show_url()
        else:
            return reverse('journals:dayentry_new')
