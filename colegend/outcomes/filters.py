import datetime

import django_filters

from colegend.scopes.models import SCOPE_CHOICES
from .models import Outcome
from .forms import OutcomeFilterForm


def filter_estimate(queryset, value):
    if value:
        if value == '1d':
            queryset = queryset.filter(estimate__lt=value)
        elif value == '1w':
            queryset = queryset.filter(estimate__range=('1d', '1w'))
        elif value == '1M':
            queryset = queryset.filter(estimate__range=('1w', '1M'))
        elif value == '12M':
            queryset = queryset.filter(estimate__gte='1M')
        elif value == '0m':
            queryset = queryset.filter(estimate__isnull=True)
    return queryset


class OutcomeFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')
    status = django_filters.ChoiceFilter(choices=(('', 'all'),) + Outcome.STATUS_CHOICES)
    scope = django_filters.ChoiceFilter(choices=(('', 'all'),) + SCOPE_CHOICES)
    ESTIMATE_CHOICES = (
        ('1d', 'hour(s)'),
        ('1w', 'day(s)'),
        ('1M', 'week(s)'),
        ('12M', 'month(s)'),
        ('0m', 'unestimated'),
    )
    estimate = django_filters.ChoiceFilter(choices=(('', 'all'),) + ESTIMATE_CHOICES, action=filter_estimate)

    class Meta:
        model = Outcome
        form = OutcomeFilterForm
        fields = ['name', 'description', 'status', 'scope']
