from django.utils import timezone


def get_current_month():
    return timezone.now().month


def get_current_year():
    return timezone.now().year
