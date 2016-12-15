from django.utils import timezone

from colegend.journals.scopes import Day


def get_current_quarter():
    return Day(timezone.now().date()).quarter.number


def get_current_year():
    return timezone.now().year
