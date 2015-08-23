from django.contrib import messages
from django.core.urlresolvers import reverse, reverse_lazy
from django.utils import timezone
from django.utils.dateparse import parse_date
from lib.views import ActiveUserRequiredMixin
from django.core.exceptions import ValidationError
from django.views.generic import DetailView, UpdateView, DeleteView, CreateView, ArchiveIndexView, RedirectView, \
    TemplateView, ListView
from journals.forms import DayEntryForm, JournalForm, WeekEntryForm
from journals.models import DayEntry, Journal, WeekEntry

__author__ = 'eraldo'


class JournalMixin(ActiveUserRequiredMixin):
    model = Journal
    form_class = JournalForm
    icon = "journal"
    tutorial = "Journal"

    def get_queryset(self):
        return super().get_queryset().owned_by(self.request.user)

    def form_valid(self, form):
        try:
            return super().form_valid(form)
        except ValidationError as e:
            # Catch model errors (e.g. unique_together).
            form.add_error(None, e)
            return super().form_invalid(form)


class JournalEditView(JournalMixin, UpdateView):
    success_url = reverse_lazy('journals:index')

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
        template = user.journal.day_template
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

    def get_object(self, queryset=None):
        # Check if date is provided.. if so use it..
        date = self.kwargs.get('date')
        if date:
            date = parse_date(date)
            try:
                return super().get_queryset().get(date=date)
            except DayEntry.DoesNotExist:
                return None
        return super().get_object(queryset)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        date = self.kwargs.get('date')
        if date:
            date = parse_date(date)
        else:
            date = self.get_object().date
        context["date"] = date
        context["previous_date"] = date - timezone.timedelta(1)
        context["next_date"] = date + timezone.timedelta(1)
        # Get user Tasks for this date.
        user = self.request.user
        scheduled_tasks = user.tasks.filter(date=date)
        deadline_projects = user.projects.filter(deadline=date)
        deadline_tasks = user.tasks.filter(deadline=date)
        done_projects = user.projects.closed().filter(completion_date__contains=date).order_by('completion_date')
        done_tasks = user.tasks.closed().filter(completion_date__contains=date).order_by('completion_date')
        created_projects = user.projects.filter(creation_date__contains=date).order_by('creation_date')
        created_tasks = user.tasks.filter(creation_date__contains=date).order_by('creation_date')
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
        trackers = user.trackers
        today = timezone.localtime(timezone.now()).date()
        # To track
        if date == today:
            context["trackers_to_track"] = trackers.to_track()
        # Tracked that day
        context["trackers_tracked"] = trackers.tracked_on(date)
        return context


class DayEntryEditView(DayEntryMixin, UpdateView):
    pass


class DayEntryDeleteView(DayEntryMixin, DeleteView):
    success_url = reverse_lazy('journals:index')
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


class WeekEntryMixin(JournalMixin):
    model = WeekEntry
    form_class = WeekEntryForm

    def get_object(self, queryset=None):
        # Check if date is provided.. if so use it..
        date = self.kwargs.get('date')
        if date:
            date = parse_date(date)
            try:
                return super().get_queryset().get(date=date)
            except WeekEntry.DoesNotExist:
                return None
        return super().get_object(queryset)


class WeekView(DayEntryMixin, TemplateView):
    template_name = "journals/week.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # date
        date = self.kwargs.get('date')
        if date:
            date = parse_date(date)
        else:
            date = timezone.now().date()
        context['date'] = date

        # week context
        week_start = date - timezone.timedelta(days=date.weekday())
        context['week_start'] = week_start
        week_end = week_start + timezone.timedelta(days=6)
        context['week_end'] = week_end
        # page title extras
        context['streak'] = self.request.user.journal.streak
        context['week_streak'] = self.request.user.journal.week_streak
        context['topic_of_the_year'] = self.request.user.journal.topic_of_the_year

        # week entry
        weekentry = WeekEntry.objects.owned_by(self.request.user).for_date(date)
        if weekentry:
            context['weekentry'] = weekentry

        # day entries
        day_entries = DayEntry.objects.owned_by(self.request.user).filter(date__range=(week_start, week_end))
        # add empty values..
        day_entries_list = []
        for day in range(0, 7):
            current_date = week_start+timezone.timedelta(days=day)
            day_entry = day_entries.filter(date=current_date)
            if day_entry:
                day_entries_list.append((current_date, day_entry.get()))
            else:
                day_entries_list.append((current_date, None))
        day_entries = day_entries_list
        context['day_entries'] = day_entries

        # paginator
        context['previous_date'] = week_start - timezone.timedelta(days=7)
        context['next_date'] = week_start + timezone.timedelta(days=7)
        return context


class WeekEntryNewView(WeekEntryMixin, CreateView):
    def get_initial(self):
        initial = super(WeekEntryNewView, self).get_initial()
        user = self.request.user
        # journal
        initial['journal'] = user.journal
        # template
        template = user.journal.week_template
        if template:
            initial['content'] = template
        # last entry
        entry = WeekEntry.objects.latest_for(user)
        if entry:
            initial['tags'] = entry.tags.all()
        # date
        try:
            new_date = self.request.GET.get('date')
        except ValueError:
            new_date = None
        if new_date:
            initial['date'] = new_date
        return initial


class WeekEntryShowView(WeekEntryMixin, DetailView):
    template_name = "journals/weekentry_show.html"


class WeekEntryEditView(WeekEntryMixin, UpdateView):
    pass


class WeekEntryDeleteView(WeekEntryMixin, DeleteView):
    success_url = reverse_lazy('journals:week')
    template_name = "confirm_delete.html"


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


class DayEntryChartView(DayEntryMixin, ListView):
    template_name = "journals/entry_chart.html"


class WeekEntryChartView(WeekEntryMixin, ListView):
    template_name = "journals/entry_chart.html"
