from django.conf import settings
from django.db import models
from django.utils import timezone
from categories.models import Category as CategoryNew

__author__ = 'eraldo'


class QuoteQuerySet(models.QuerySet):
    def accepted(self):
        return self.filter(accepted=True)

    def daily_quote(self, date=None):
        # Use only accepted quotes.
        quotes = self.accepted()

        # Fetch past quote if a date was given.
        if date:
            try:
                return quotes.get(used_as_daily=date)
            except Quote.DoesNotExist:
                return None

        # Get or assign today's quote:
        # Check if there already is a quote for today
        # If not..
        # then assign one using a 'new' quote.
        # If there are no new ones..
        # then use the last used quote.

        today = timezone.datetime.today().date()
        try:
            current_quote = quotes.get(used_as_daily=today)
        except Quote.DoesNotExist:
            # There is no quote for today yet.. so assign one.
            current_quote = quotes.order_by('used_as_daily').first()
            current_quote.used_as_daily = today
            current_quote.save()
        return current_quote


class Quote(models.Model):
    """A motivational text quote."""

    name = models.CharField(max_length=100, unique=True, help_text="What is the quote about?")
    text = models.TextField()
    author = models.CharField(max_length=100, default="Someone")
    category = models.ForeignKey(CategoryNew)
    provider = models.ForeignKey(settings.AUTH_USER_MODEL)
    accepted = models.BooleanField(default=False)
    used_as_daily = models.DateField(null=True, blank=True, unique=True)

    objects = QuoteQuerySet.as_manager()

    def __str__(self):
        return self.name
