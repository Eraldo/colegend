from django.db import models
from django.db.models import QuerySet
from django.utils import timezone
from markitup.fields import MarkupField
from categories.models import Category
from lib.models import OwnedBase, TimeStampedBase, TrackedBase, OwnedQueryMixin, AutoUrlMixin


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
    notes = models.TextField(blank=True)
    url = models.URLField(blank=True)

    objects = TrackerQuerySet.as_manager()

    class Meta:
        ordering = ['status']

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


class Joke(OwnedBase, AutoUrlMixin, TimeStampedBase):
    name = models.CharField(max_length=100)
    description = models.TextField()
    rating = models.PositiveSmallIntegerField(default=0)
    notes = models.TextField(blank=True)

    objects = TrackerQuerySet.as_manager()

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
