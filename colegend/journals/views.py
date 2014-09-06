from braces.views import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.views.generic import DetailView, UpdateView, DeleteView, CreateView, ArchiveIndexView
from journals.forms import DayEntryForm
from journals.models import DayEntry
from lib.views import OwnedItemsMixin

__author__ = 'eraldo'


class DayEntryMixin(LoginRequiredMixin, OwnedItemsMixin):
    model = DayEntry
    form_class = DayEntryForm


class DayEntryListView(DayEntryMixin, ArchiveIndexView):
    date_field = "date"
    template_name = "journals/dayentry_list.html"


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
