from django.contrib import messages
from django.core.urlresolvers import reverse, reverse_lazy
from django.utils import timezone
from django.utils.dateparse import parse_date
from lib.views import ActiveUserRequiredMixin
from django.core.exceptions import ValidationError
from django.views.generic import DetailView, UpdateView, DeleteView, CreateView, ArchiveIndexView, RedirectView, \
    TemplateView, ListView
from journals.forms import DayEntryForm, JournalForm
from journals.models import DayEntry, Journal

__author__ = 'eraldo'


class JournalMixin(ActiveUserRequiredMixin):
    model = Journal
    form_class = JournalForm
    icon = "journal"
    tutorial = "Journal"

    def get_queryset(self):
        return super().get_queryset().owned_by(self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        try:
            return super().form_valid(form)
        except ValidationError as e:
            # Catch model errors (e.g. unique_together).
            form.add_error(None, e)
            return super().form_invalid(form)


class JournalEditView(JournalMixin, UpdateView):
    success_url = reverse_lazy('journals:dayentry_list')

    def get_object(self, queryset=None):
        return self.request.user.journal


class DayEntryMixin(JournalMixin):
    model = DayEntry
    form_class = DayEntryForm


class DayEntryListView(DayEntryMixin, ArchiveIndexView):
    date_field = "date"
    template_name = "journals/dayentry_list.html"
    allow_empty = True
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(DayEntryListView, self).get_context_data(**kwargs)
        context['total_counter'] = self.get_queryset().count()
        context['streak'] = self.request.user.journal.streak
        context['topic_of_the_year'] = self.request.user.journal.topic_of_the_year
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
        template = user.journal.template
        if template:
            initial['content'] = template
        # location
        entry = DayEntry.objects.latest_for(user)
        if entry:
            initial['location'] = entry.location
            initial['tags'] = entry.tags.all()
        # date
        try:
            new_date = self.request.GET.get('date')
        except ValueError:
            new_date = None
        if new_date:
            initial['date'] = new_date
        return initial


class DayEntryShowView(DayEntryMixin, DetailView):
    template_name = "journals/dayentry_show.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get user Tasks for this date.
        entry = self.get_object()
        user = self.request.user
        scheduled_tasks = user.tasks.filter(date=entry.date)
        deadline_projects = user.projects.filter(deadline=entry.date)
        deadline_tasks = user.tasks.filter(deadline=entry.date)
        done_projects = user.projects.closed().filter(completion_date__contains=entry.date).order_by('completion_date')
        done_tasks = user.tasks.closed().filter(completion_date__contains=entry.date).order_by('completion_date')
        created_projects = user.projects.filter(creation_date__contains=entry.date).order_by('creation_date')
        created_tasks = user.tasks.filter(creation_date__contains=entry.date).order_by('creation_date')
        day_tasks = scheduled_tasks or deadline_tasks or done_tasks or created_tasks
        if day_tasks:
            context["day_tasks"] = day_tasks
            if scheduled_tasks:
                context["scheduled_tasks"] = scheduled_tasks
            if deadline_tasks:
                context["deadline_tasks"] = deadline_tasks
            if deadline_projects:
                context["deadline_projects"] = deadline_projects
            if done_projects:
                context["done_projects"] = done_projects
            if done_tasks:
                context["done_tasks"] = done_tasks
            if created_projects:
                context["created_projects"] = created_projects
            if created_tasks:
                context["created_tasks"] = created_tasks
        # TRACKERS
        trackers = user.tracker_set
        today = timezone.localtime(timezone.now()).date()
        # To track
        if entry.date == today:
            context["trackers_to_track"] = trackers.to_track()
        # Tracked that day
        context["trackers_tracked"] = trackers.tracked_on(entry.date)
        # missing date
        previous_date = entry.get_previous()
        next_date = entry.get_next()
        one_day = timezone.timedelta(1)
        ## next day missing
        if next_date and next_date.date != entry.date + one_day or \
                not next_date and entry.date < today:
            context["missing"] = entry.date + one_day
        ## previous day missing
        elif previous_date and previous_date.date != entry.date - one_day:
            context["missing"] = entry.date - one_day
        return context


class DayEntryEditView(DayEntryMixin, UpdateView):
    pass


class DayEntryDeleteView(DayEntryMixin, DeleteView):
    success_url = reverse_lazy('journals:dayentry_list')
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


class MapView(DayEntryMixin, TemplateView):
    template_name = "journals/map.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        locations = self.request.user.journal.entries.values_list('location', flat=True)
        location_set = set()
        for location_string in locations:
            for location in location_string.split(';'):
                location_set.add(location.strip())
        context['locations'] = location_set
        context['total_counter'] = len(location_set)
        return context

    def get(self, request, *args, **kwargs):
        message = "Info: The travel map can need quite some time to load."
        messages.add_message(self.request, messages.INFO, message)
        return super().get(self.request, *args, **kwargs)


class EntryChartView(DayEntryMixin, ListView):
    template_name = "journals/entry_chart.html"
