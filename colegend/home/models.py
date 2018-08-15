from enum import Enum

from django.conf import settings
from django.core.validators import MaxValueValidator
from django.db import models

# Create your models here.
from django.db.models import Sum, Q
from django.shortcuts import redirect
from django.utils import timezone
from ordered_model.models import OrderedModel
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page
from wagtail.search import index

from colegend.cms.blocks import BASE_BLOCKS
from colegend.core.fields import MarkdownField
from colegend.core.intuitive_duration.modelfields import IntuitiveDurationField
from colegend.core.models import TimeStampedBase, OwnedBase
from colegend.core.templatetags.core_tags import link

from django.utils.translation import ugettext_lazy as _

from colegend.office.models import AgendaPage
from colegend.scopes.models import ScopeField, get_scope_by_name, Scope


class ControlledHabit(Enum):
    DASHBOARD_HABIT = 'Dashboard'
    JOURNAL_HABIT = 'Journal'
    FOCUS_HABIT = 'Focus'
    STATS_HABIT = 'Stats'


controlled_habits_data = {
    ControlledHabit.DASHBOARD_HABIT: {
        'name': ControlledHabit.DASHBOARD_HABIT.value,
        'is_controlled': True,
        'duration': timezone.timedelta(seconds=10),
        'icon': '🗞️',
        'content': 'Checking my coLegend Dashboard.'
    },
    ControlledHabit.JOURNAL_HABIT: {
        'name': ControlledHabit.JOURNAL_HABIT.value,
        'is_controlled': True,
        'icon': '📖',
        'content': 'Writing my journal entry.'
    },
    ControlledHabit.STATS_HABIT: {
        'name': ControlledHabit.STATS_HABIT.value,
        'is_controlled': True,
        'icon': '📊',
        'content': 'Scanning my life areas.'
    },
    ControlledHabit.FOCUS_HABIT: {
        'name': ControlledHabit.FOCUS_HABIT.value,
        'is_controlled': True,
        'icon': '🎯',
        'content': 'Setting my focus.'
    }
}


def get_controlled_habit(user, controlled_habit: ControlledHabit):
    """
    Get the user's controlled habit matching the habit name.
    Only prefedined controlled habit names are valid.

    :param user: The user who's habit is to be fetched.
    :param habit_name: The name of the controlled habit.
    :return: The controlled habit instance.
    """
    habit_data = controlled_habits_data.get(controlled_habit)
    if not habit_data:
        raise Exception(f'No controlled habit named "{controlled_habit}" was found.')

    try:
        habit = user.habits.get(name=controlled_habit.value, is_controlled=True)
    except Habit.DoesNotExist:
        habit = user.habits.create(**habit_data)
    return habit


class HabitQuerySet(models.QuerySet):
    def active(self):
        return self.filter(is_active=True)

    def controlled(self):
        return self.filter(is_controlled=True)

    def untracked(self):
        """
        Filters the queryset to only habits that have not been tracked successfully within the their current scope period.

        :return: Untracked habits
        """

        # Getting all scopes.
        day_scope = get_scope_by_name(Scope.DAY.value)()
        week_scope = get_scope_by_name(Scope.WEEK.value)()
        month_scope = get_scope_by_name(Scope.MONTH.value)()
        year_scope = get_scope_by_name(Scope.YEAR.value)()

        return self.exclude(
            Q(scope=day_scope.name, track_events__created__date__range=(day_scope.start, day_scope.end)) |
            Q(scope=week_scope.name, track_events__created__date__range=(week_scope.start, week_scope.end)) |
            Q(scope=month_scope.name, track_events__created__date__range=(month_scope.start, month_scope.end)) |
            Q(scope=year_scope.name, track_events__created__date__range=(year_scope.start, year_scope.end))
        )

    def tracked(self):
        """
        Filters the queryset to only habits that have been tracked successfully within the their current scope period.

        :return: Tracked habits
        """

        # Getting all scopes.
        day_scope = get_scope_by_name(Scope.DAY.value)()
        week_scope = get_scope_by_name(Scope.WEEK.value)()
        month_scope = get_scope_by_name(Scope.MONTH.value)()
        year_scope = get_scope_by_name(Scope.YEAR.value)()

        return self.filter(
            Q(scope=day_scope.name, track_events__created__date__range=(day_scope.start, day_scope.end)) |
            Q(scope=week_scope.name, track_events__created__date__range=(week_scope.start, week_scope.end)) |
            Q(scope=month_scope.name, track_events__created__date__range=(month_scope.start, month_scope.end)) |
            Q(scope=year_scope.name, track_events__created__date__range=(year_scope.start, year_scope.end))
        )

    def search(self, query):
        queryset = self.filter(Q(name__icontains=query) | Q(content__icontains=query) | Q(content__icontains=query))
        return queryset


class Habit(OwnedBase, TimeStampedBase, OrderedModel):
    name = models.CharField(
        _('name'),
        max_length=255,
    )
    scope = ScopeField()
    icon = models.CharField(
        _('icon'),
        max_length=6,
        blank=True,
    )
    duration = IntuitiveDurationField(
        _('duration'),
        default=timezone.timedelta(minutes=10),
    )
    content = MarkdownField(
        verbose_name=_('content'),
        blank=True
    )
    is_active = models.BooleanField(
        verbose_name=_('active'),
        default=True,
    )
    is_controlled = models.BooleanField(
        verbose_name=_('controlled'),
        default=False,
        help_text=_(
            'Designates whether this habit is controlled by the system.'
        ),
    )
    streak = models.PositiveSmallIntegerField(
        _('streak'),
        default=0,
    )
    streak_max = models.PositiveSmallIntegerField(
        _('best streak'),
        default=0,
    )

    @property
    def is_tracked(self):
        return self.has_track()

    def track(self):
        """
        Create a track record for this habit if not already present.
        And update the streak on successful track creation.
        :return:
            `track`: On tracking success
        """
        if not self.has_track():
            today = timezone.localtime(timezone.now()).date()
            # Create the new track record.
            track, created = self.track_events.get_or_create(created__date=today)
            if created:
                self.increase_streak()
                return track

    def has_track(self, date=None):
        """
        Check if a track record already exists (for the given date or today).
        :param date: The date to check for: If a track exists?
        :return: True if a track event was found. False if not found.
        """
        if date is None:
            date = timezone.localtime(timezone.now()).date()
            scope = get_scope_by_name(self.scope)(date)
        else:
            scope = get_scope_by_name(self.scope)()
        return self.track_events.filter(created__date__range=(scope.start, scope.end)).exists()

    def reset_streak(self, to=0):
        """
        Reset the streak and update the maximum streak if the new one is higher.
        :param to:
        :return:
        """
        updated_fields = ['streak']
        if self.streak > self.streak_max:
            self.streak_max = self.streak
            updated_fields += ['streak_max']
        self.streak = to
        self.save(update_fields=updated_fields)

    def increase_streak(self):
        self.streak += 1
        # Update max streak
        if self.streak > self.streak_max:
            self.streak_max = self.streak

    def get_stats(self, phases=4):
        """
        Check the last X phases for completion.

        Example:
            Performance of last 4 weeks?
            Result: [0, 1, 1, 0]
            => Not yet a success this week, success the 2 weeks before, no success 3 weeks ago.

        Result type: [{this_phase}, {last_phase}, {pre_last_phase}, {pre_pre_last_phase}]
        """
        # TODO: Refactor to static variables plus updates. (signals?).

        scope = get_scope_by_name(self.scope)()
        stats = [0 for x in range(phases)]  # [0, 0, 0, ...] empty result array

        for phase in range(phases):  # for each phase
            start = scope.start
            end = scope.end
            stats[phase] = self.track_events.filter(created__date__range=(start, end)).count()
            scope = scope.previous

        return stats

    # Reverse: owner, reminders, track_events

    order_with_respect_to = 'owner'

    objects = HabitQuerySet.as_manager()

    class Meta(OrderedModel.Meta):
        default_related_name = 'habits'

    def __str__(self):
        return self.name


class HabitTrackEvent(TimeStampedBase):
    habit = models.ForeignKey(
        to=Habit,
        on_delete=models.CASCADE
    )

    class Meta:
        default_related_name = 'track_events'

    def __str__(self):
        return f'[{self.created}] {self.habit}'


class HabitReminder(TimeStampedBase):
    habit = models.ForeignKey(
        to=Habit,
        on_delete=models.CASCADE
    )

    # Day?: Time
    time = models.TimeField(
        _('time'),
    )

    # Week?: Weekdays
    # monday = models.BooleanField(
    #     verbose_name=_('Monday'),
    #     default=True
    # )
    # tuesday = models.BooleanField(
    #     verbose_name=_('Tuesday'),
    #     default=True
    # )
    # # etc
    # Or: https://github.com/goinnn/django-multiselectfield

    # Alternative: Using CRON syntax?
    # cron = models.CharField(
    #     _('date'),
    # )

    # Month?: Date (on day 21.) | on first/second/etc Weekday
    # date = models.DateField(
    #     _('date'),
    # )

    class Meta:
        default_related_name = 'reminders'

    def __str__(self):
        return f'{self.time}'


class Routine(OwnedBase, TimeStampedBase, OrderedModel):
    name = models.CharField(
        _('name'),
        max_length=255,
    )
    scope = ScopeField()
    content = MarkdownField(
        verbose_name=_('content'),
        blank=True
    )

    habits = models.ManyToManyField(
        to=Habit, through='RoutineHabit')

    # Reverse: owner, reminders
    # TODO: Related reminders

    @property
    def duration(self):
        return self.habits.aggregate(duration=Sum('duration')).get('duration')

    order_with_respect_to = 'owner'

    class Meta(OrderedModel.Meta):
        default_related_name = 'routines'

    def __str__(self):
        return self.name


class RoutineHabit(OrderedModel):
    routine = models.ForeignKey(Routine, on_delete=models.CASCADE)
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE)
    order_with_respect_to = 'routine'

    class Meta:
        ordering = ('routine', 'order')
        default_related_name = 'routine_habits'
        unique_together = ['routine', 'habit']
        # TODO: Check if unique together is needed here.

    def __str__(self):
        return f'{self.routine}/{self.habit}'


class Scan(OwnedBase, TimeStampedBase):
    date = models.DateField(
        _('date'),
        default=timezone.now
    )
    area_1 = models.PositiveSmallIntegerField(
        _('area 1'),
        validators=[MaxValueValidator(100)]
    )
    area_2 = models.PositiveSmallIntegerField(
        _('area 2'),
        validators=[MaxValueValidator(100)]
    )
    area_3 = models.PositiveSmallIntegerField(
        _('area 3'),
        validators=[MaxValueValidator(100)]
    )
    area_4 = models.PositiveSmallIntegerField(
        _('area 4'),
        validators=[MaxValueValidator(100)]
    )
    area_5 = models.PositiveSmallIntegerField(
        _('area 5'),
        validators=[MaxValueValidator(100)]
    )
    area_6 = models.PositiveSmallIntegerField(
        _('area 6'),
        validators=[MaxValueValidator(100)]
    )
    area_7 = models.PositiveSmallIntegerField(
        _('area 7'),
        validators=[MaxValueValidator(100)]
    )

    class Meta:
        verbose_name = _('scan')
        verbose_name_plural = _('scans')
        default_related_name = 'scans'
        unique_together = ['owner', 'date']
        get_latest_by = 'date'
        ordering = ['-date']

    def __str__(self):
        return 'Scan {0}'.format(self.date)


class HomePage(Page):
    template = 'home/index.html'

    def serve(self, request, *args, **kwargs):
        return redirect(self.get_first_child().url)

    parent_page_types = ['cms.RootPage']
    subpage_types = ['DashboardPage', 'HabitsPage', 'StatsPage']


class DashboardPage(Page):
    template = 'home/dashboard.html'

    content = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('content', classname="full"),
    ]

    parent_page_types = ['HomePage']
    subpage_types = []

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['next_step'] = self.get_next_step(request.user)
        return context

    def get_next_step(self, user):
        today = timezone.localtime(timezone.now()).date()

        # Has the user set his focus?
        focus = user.focuses.filter(scope=Scope.DAY.value, start=today)
        agenda_page = AgendaPage.objects.first()
        if not focus and agenda_page:
            url = agenda_page.url + '?scope=day&date={}'.format(today)
            return link(_('Setting focus'), url)

        # Has the user written his journal entry?
        dayentry = user.journal_entries.filter(scope=Scope.DAY.value, start=today)
        if not dayentry:
            return link(_('Create a journal entry'), '#')

    def __str__(self):
        return self.title


class HabitsPage(Page):
    template = 'home/habits.html'

    content = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('content', classname="full"),
    ]

    parent_page_types = ['HomePage']
    subpage_types = []


class StatsPage(Page):
    template = 'home/stats.html'

    content = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('content', classname="full"),
    ]

    parent_page_types = ['HomePage']
    subpage_types = []


class JoinPage(Page):
    template = 'home/join.html'

    content = StreamField(BASE_BLOCKS, blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('content'),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('content'),
    ]

    class Meta:
        verbose_name = _('Join')

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['open'] = True
        if settings.ACCOUNT_ALLOW_REGISTRATION:
            context['open'] = True
        return context
