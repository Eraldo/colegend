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
        context['total_counter'] = self.get_queryset().count()
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get user Tasks for this date.
        entry = self.get_object()
        user = self.request.user
        scheduled_tasks = user.tasks.filter(date=entry.date)
        deadline_tasks = user.tasks.filter(deadline=entry.date)
        done_tasks = user.tasks.closed().filter(completion_date__contains=entry.date).order_by('completion_date')
        created_tasks = user.tasks.filter(creation_date__contains=entry.date).order_by('creation_date')
        day_tasks = scheduled_tasks or deadline_tasks or done_tasks or created_tasks
        if day_tasks:
            context["day_tasks"] = day_tasks
            if scheduled_tasks:
                context["scheduled_tasks"] = scheduled_tasks
            if deadline_tasks:
                context["deadline_tasks"] = deadline_tasks
            if done_tasks:
                context["done_tasks"] = done_tasks
            if created_tasks:
                context["created_tasks"] = created_tasks
        return context


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
