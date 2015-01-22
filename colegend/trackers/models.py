from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator
from django.db import models
from django.db.models import QuerySet
from django.utils import timezone
from django.utils.timesince import timesince
from markitup.fields import MarkupField
from categories.models import Category
from lib.models import OwnedBase, TimeStampedBase, TrackedBase, OwnedQueryMixin, AutoUrlMixin
from lib.validators import validate_datetime_in_past, validate_date_today_or_in_past


class TrackerQuerySet(OwnedQueryMixin, QuerySet):
    pass


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
    tags = models.CharField(max_length=100)
    notes = models.TextField(blank=True)

    objects = TrackerQuerySet.as_manager()

    def __str__(self):
        return "{time} €{amount}".format(time=self.time, amount=self.amount)


class Dream(OwnedBase, AutoUrlMixin, TimeStampedBase):
    date = models.DateField(default=timezone.now)
    name = models.CharField(max_length=100)
    description = MarkupField(blank=True)
    symbols = models.CharField(max_length=100, blank=True, help_text="Topics? Nouns?")

    objects = TrackerQuerySet.as_manager()

    def __str__(self):
        return "{date}: {name}".format(date=self.date, name=self.name)


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
        return str(self.duration)[:-3]

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

    @property
    def duration(self):
        if self.end:
            return self.end - self.start

    def get_duration_display(self):
        if not self.duration:
            return
        return timesince(self.start, self.end)
        return str(self.duration)[:-3]

    def clean(self, *args, **kwargs):
        """
        Make sure that the end time is after the start time.
        """
        if self.end and self.end <= self.start:
            raise ValidationError({'end': ["End time needs to be after start time."]})
        super().clean(*args, **kwargs)


TRACKERS = [Sleep, Weight, Sex, Transaction, Walk, Joke, Book, Dream]
