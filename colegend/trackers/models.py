from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models import QuerySet, Sum
from django.utils import timezone
from django.utils.timesince import timesince
from markitup.fields import MarkupField
from categories.models import Category
from lib.models import OwnedBase, TimeStampedBase, TrackedBase, OwnedQueryMixin, AutoUrlMixin, ValidateModelMixin
from lib.validators import validate_datetime_in_past, validate_date_today_or_in_past, validate_date_within_one_week


class TrackerQuerySet(OwnedQueryMixin, QuerySet):
    def to_track(self):
        pks = []
        for tracker in self.exclude(frequency=Tracker.UNKNOWN):
            if not tracker.is_tracked:
                pks.append(tracker.pk)
        return self.filter(pk__in=pks)

    def tracked(self):
        pks = []
        for tracker in self.all():
            if tracker.is_tracked:
                pks.append(tracker.pk)
        return self.filter(pk__in=pks)

    def tracked_on(self, date):
        pks = []
        for tracker in self.all():
            if tracker.data.filter(date=date):
                pks.append(tracker.pk)
        return self.filter(pk__in=pks)

    def tracked_today(self):
        return self.tracked_on(timezone.now().date())


class Tracker(OwnedBase, AutoUrlMixin, TimeStampedBase):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category)
    CHECK = 0
    NUMBER = 1
    RATING = 2
    TYPE_CHOICES = (
        (CHECK, "Check"),
        (NUMBER, "Number"),
        (RATING, "Rating"),
    )
    tracker_type = models.PositiveSmallIntegerField(verbose_name="Type", choices=TYPE_CHOICES, default=0)
    UNKNOWN = 0
    DAILY = 1
    WEEKLY = 2
    MONTHLY = 3
    FREQUENCY_CHOICES = (
        (DAILY, "Daily"),
        (WEEKLY, "Weekly"),
        (MONTHLY, "Monthly"),
        (UNKNOWN, "Unknown"),
    )
    frequency = models.PositiveSmallIntegerField(choices=FREQUENCY_CHOICES, default=1)
    CALENDAR_CHART = 0
    COLUMN_CHART = 1
    LINE_CHART = 2
    CHART_TYPE_CHOICES = (
        (CALENDAR_CHART, "Calendar Chart"),
        (COLUMN_CHART, "Column Chart"),
        (LINE_CHART, "Line Chart"),
    )
    chart_type = models.PositiveSmallIntegerField(choices=CHART_TYPE_CHOICES, default=0)

    objects = TrackerQuerySet.as_manager()

    def __str__(self):
        return self.name

    @property
    def data(self):
        if self.tracker_type == self.CHECK:
            return self.checkdata_set.all()
        if self.tracker_type == self.NUMBER:
            return self.numberdata_set.all()
        if self.tracker_type == self.RATING:
            return self.ratingdata_set.all()

    @property
    def is_tracked(self):
        last_data = self.data.first()
        if not last_data:
            return False
        today = timezone.now().date()
        if self.frequency == Tracker.DAILY:
            return last_data.date == today
        elif self.frequency == Tracker.WEEKLY:
            return last_data.date >= today - timezone.timedelta(today.weekday())
        elif self.frequency == Tracker.MONTHLY:
            return last_data.date > today - timezone.timedelta(today.day)

    def get_chain(self, days=7):
        """
        Return a series of 'True' and 'False' for the last week.
        Starting and including today.
        """
        chain = []
        today = timezone.now().date()
        data = self.data.filter(date__range=[today - timezone.timedelta(days=days), today])
        if not data:
            return [False for n in range(7)]
        dates = data.values_list('date', flat=True)
        for days_ago in range(0, days):
            day = today - timezone.timedelta(days=days_ago)
            if day in dates:
                chain.append(True)
            else:
                chain.append(False)
        return chain


class BaseData(ValidateModelMixin, models.Model):
    tracker = models.ForeignKey(Tracker)
    date = models.DateField(default=timezone.now,
                            validators=[validate_date_today_or_in_past, validate_date_within_one_week])

    class Meta:
        ordering = ['-date']
        unique_together = ("tracker", "date")
        abstract = True

    def get_delete_url(self):
        return reverse("trackers:data_delete", kwargs={"tracker_pk": self.tracker.pk, "pk": self.pk})


class CheckData(BaseData):
    @property
    def value(self):
        return "1"

    def __str__(self):
        return "{}: ✓".format(self.date)


class NumberData(BaseData):
    number = models.IntegerField()

    @property
    def value(self):
        return self.number

    def __str__(self):
        return "{}: {}".format(self.date, self.number)


class RatingData(BaseData):
    rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    @property
    def value(self):
        return self.rating

    def __str__(self):
        return "{}: {}".format(self.date, self.rating)


class Weight(OwnedBase, AutoUrlMixin, TimeStampedBase):
    time = models.DateTimeField(default=timezone.now)
    weight = models.PositiveSmallIntegerField()
    notes = models.TextField(blank=True)

    objects = TrackerQuerySet.as_manager()

    class Meta:
        verbose_name_plural = "Weight"
        ordering = ['-time']

    def __str__(self):
        return "{time}: {weight}kg".format(time=self.time, weight=self.weight)

    @property
    def value(self):
        return self.weight


class Sex(OwnedBase, AutoUrlMixin, TimeStampedBase):
    date = models.DateField(default=timezone.now)
    amount = models.PositiveSmallIntegerField(default=1)
    person = models.CharField(max_length=100)
    notes = models.TextField(blank=True)

    objects = TrackerQuerySet.as_manager()

    class Meta:
        verbose_name_plural = "Sex"
        ordering = ['-date']

    def __str__(self):
        return "{date}: {amount}x [{person}]".format(date=self.date, amount=self.amount, person=self.person)

    @property
    def value(self):
        return self.amount


class Book(OwnedBase, AutoUrlMixin, TrackedBase):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    NEXT = 0
    TODO = 1
    MAYBE = 2
    DONE = 3
    CANCELED = 4
    STATUS_CHOICES = (
        (NEXT, "Next"),
        (TODO, "Todo"),
        (MAYBE, "Maybe"),
        (DONE, "Done"),
        (CANCELED, "Canceled"),
    )
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES, default=1)
    BOOK = 0
    EBOOK = 1
    AUDIO_BOOK = 2
    TYPE_CHOICES = (
        (BOOK, "Book"),
        (EBOOK, "E-Book"),
        (AUDIO_BOOK, "Audio-Book"),
    )
    book_type = models.PositiveSmallIntegerField(verbose_name="Type", choices=TYPE_CHOICES, default=0)
    category = models.ForeignKey(Category)
    start_date = models.DateField(null=True, blank=True, validators=[validate_date_today_or_in_past])
    end_date = models.DateField(null=True, blank=True, validators=[validate_date_today_or_in_past])
    origin = models.CharField(blank=True, max_length=100)
    rating = models.PositiveSmallIntegerField(default=0, validators=[MaxValueValidator(5)])
    url = models.URLField(blank=True)
    notes = models.TextField(blank=True)
    feedback = models.TextField(blank=True)

    objects = TrackerQuerySet.as_manager()

    class Meta:
        ordering = ['status', '-rating']

    def __str__(self):
        return "{title} [{author}]".format(title=self.title, author=self.author)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.old_status = self.status

    def save(self, *args, **kwargs):
        # Track status changes.
        if self.status != self.old_status:
            message = "Status set to '{}'.".format(self.get_status_display())
            self.log(message)
        super().save(*args, **kwargs)
        self.old_status = self.status

    def has_url(self):
        return bool(self.url)

    has_url.boolean = True
    has_url.short_description = "Url"

    def clean(self, *args, **kwargs):
        """
        Make sure that the end date is after the start date.
        """
        if self.end_date and not self.start_date:
            raise ValidationError({'start_date': ["You need to have a start date in order to set an end date."]})
        elif self.end_date and self.end_date < self.start_date:
            raise ValidationError({'end_date': ["End date needs to be on the same day or after the start date."]})
        super().clean(*args, **kwargs)


class Joke(OwnedBase, AutoUrlMixin, TimeStampedBase):
    name = models.CharField(max_length=100)
    description = models.TextField()
    rating = models.PositiveSmallIntegerField(default=0, validators=[MaxValueValidator(5)])
    notes = models.TextField(blank=True)

    objects = TrackerQuerySet.as_manager()

    class Meta:
        ordering = ['-rating']

    def __str__(self):
        return self.name


class TransactionQueryset(TrackerQuerySet):
    @property
    def balance(self):
        return self.aggregate(Sum('amount')).get("amount__sum")

    def expenses(self):
        return self.filter(transaction_type=Transaction.EXPENSE)

    def incomes(self):
        return self.filter(transaction_type=Transaction.INCOME)

    def category(self, category):
        if isinstance(category, Category):
            return self.filter(category=category)


class Transaction(OwnedBase, AutoUrlMixin, TimeStampedBase):
    time = models.DateTimeField(default=timezone.now)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    EXPENSE = 1
    INCOME = 2
    TYPE_CHOICES = (
        (EXPENSE, "Expense"),
        (INCOME, "Income"),
    )
    transaction_type = models.PositiveSmallIntegerField(verbose_name="Type", choices=TYPE_CHOICES, default=1)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category)
    tags = models.CharField(max_length=100, blank=True)
    notes = models.TextField(blank=True)

    objects = TransactionQueryset.as_manager()

    class Meta:
        ordering = ['-time']

    def __str__(self):
        return "{time} €{amount}".format(time=self.time, amount=self.amount)

    @property
    def value(self):
        if self.transaction_type == Transaction.EXPENSE:
            return - self.amount
        elif self.transaction_type == Transaction.INCOME:
            return self.amount


class Dream(OwnedBase, AutoUrlMixin, TimeStampedBase):
    date = models.DateField(default=timezone.now)
    name = models.CharField(max_length=100)
    description = MarkupField(blank=True)
    symbols = models.CharField(max_length=100, blank=True, help_text="Topics? Nouns?")

    objects = TrackerQuerySet.as_manager()

    def __str__(self):
        return "{date}: {name}".format(date=self.date, name=self.name)

    class Meta:
        ordering = ['-date']

    @property
    def value(self):
        return 1


class Sleep(OwnedBase, AutoUrlMixin, TimeStampedBase):
    start = models.DateTimeField(validators=[validate_datetime_in_past])
    end = models.DateTimeField(null=True, blank=True, validators=[validate_datetime_in_past])
    notes = models.TextField(blank=True)

    objects = TrackerQuerySet.as_manager()

    class Meta:
        ordering = ['-start']

    def __str__(self):
        return "{start}-{end}".format(start=self.start, end=self.end)

    @property
    def duration(self):
        if self.end:
            return self.end - self.start

    def get_duration_display(self):
        if not self.duration:
            return
        return timesince(self.start, self.end)

    @property
    def value(self):
        return round(self.duration.total_seconds() / 3600, 1)

    def clean(self, *args, **kwargs):
        """
        Make sure that the end time is after the start time.
        """
        if self.end and self.end <= self.start:
            raise ValidationError({'end': ["End time needs to be after start time."]})
        super().clean(*args, **kwargs)


class Walk(OwnedBase, AutoUrlMixin, TimeStampedBase):
    start = models.DateTimeField(validators=[validate_datetime_in_past])
    end = models.DateTimeField(null=True, blank=True, validators=[validate_datetime_in_past])
    notes = models.TextField(blank=True)

    objects = TrackerQuerySet.as_manager()

    def __str__(self):
        return "{start}-{end}".format(start=self.start, end=self.end)

    class Meta:
        ordering = ['-start']

    @property
    def duration(self):
        if self.end:
            return self.end - self.start

    def get_duration_display(self):
        if not self.duration:
            return
        return timesince(self.start, self.end)

    @property
    def value(self):
        if self.duration:
            return self.duration.total_seconds() / 60
        else:
            return 0

    def clean(self, *args, **kwargs):
        """
        Make sure that the end time is after the start time.
        """
        if self.end and self.end <= self.start:
            raise ValidationError({'end': ["End time needs to be after start time."]})
        super().clean(*args, **kwargs)


TRACKERS = [Sleep, Weight, Sex, Transaction, Walk, Joke, Book, Dream]
