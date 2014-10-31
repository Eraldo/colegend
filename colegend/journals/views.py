from lib.views import ActiveUserRequiredMixin
from django.core.exceptions import ValidationError
from django.views.generic import DetailView, UpdateView, DeleteView, CreateView, ArchiveIndexView
from journals.forms import DayEntryForm
from journals.models import DayEntry
from lib.views import OwnedItemsMixin

__author__ = 'eraldo'


class DayEntryMixin(ActiveUserRequiredMixin, OwnedItemsMixin):
    model = DayEntry
    form_class = DayEntryForm

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

    def get_context_data(self, **kwargs):
        context = super(DayEntryListView, self).get_context_data(**kwargs)
        context['streak'] = DayEntry.objects.streak_for(self.request.user)
        return context


class DayEntryNewView(DayEntryMixin, CreateView):
    # success_url = reverse_lazy('tags:tag_list')

    def form_valid(self, form):
        user = self.request.user
        form.instance.owner = user
        return super(DayEntryNewView, self).form_valid(form)

    def get_initial(self):
        initial = super(DayEntryNewView, self).get_initial()
        user = self.request.user
        # template
        entry_template = user.settings.journal_entry_template
        if entry_template:
            initial['text'] = entry_template
        # location
        location = DayEntry.objects.latest_for(user).location
        if location:
            initial['location'] = location
        return initial


class DayEntryShowView(DayEntryMixin, DetailView):
    template_name = "journals/dayentry_show.html"


class DayEntryEditView(DayEntryMixin, UpdateView):
    pass


class DayEntryDeleteView(DayEntryMixin, DeleteView):
    pass
