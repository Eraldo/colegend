from braces.views import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.views.generic import DetailView, UpdateView, DeleteView, CreateView, ArchiveIndexView
from journals.forms import DayEntryForm
from journals.models import DayEntry
from lib.views import OwnedItemsMixin

__author__ = 'eraldo'


class DayEntryMixin(LoginRequiredMixin, OwnedItemsMixin):
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


class DayEntryNewView(DayEntryMixin, CreateView):
    # success_url = reverse_lazy('tags:tag_list')

    def form_valid(self, form):
        user = self.request.user
        form.instance.owner = user
        return super(DayEntryNewView, self).form_valid(form)


class DayEntryShowView(DayEntryMixin, DetailView):
    template_name = "journals/dayentry_show.html"


class DayEntryEditView(DayEntryMixin, UpdateView):
    pass


class DayEntryDeleteView(DayEntryMixin, DeleteView):
    pass
