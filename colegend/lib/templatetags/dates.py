from django import template
from django.utils import timezone

__author__ = 'eraldo'

register = template.Library()

@register.filter(name='due_date')
def get_due_date_string(value):
    delta = value - timezone.now().date()

    if -7 <= delta.days <= 7:
        if delta.days == 0:
            return "Today"
        elif delta.days < 1:
            return "%s %s ago" % (abs(delta.days),
                ("day" if abs(delta.days) == 1 else "days"))
        elif delta.days == 1:
            return "Tomorrow"
        elif delta.days > 1:
            return "In %s days" % delta.days
    return value

@register.filter(name='date_tense')
def get_date_tense(value):
    if not value:
        return

    delta = value - timezone.now().date()

    if delta.days < -7:
        return "past"
    elif delta.days < 0:
        return "near-past"
    elif delta.days == 0:
        return "present"
    elif delta.days <= 7:
        return "near-future"
    elif delta.days > 7:
        return "future"
