import django_filters
from graphql_relay import from_global_id

from .models import Outcome, Step


def filter_estimate(queryset, name, value):
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
    # name = django_filters.CharFilter(lookup_expr='icontains')
    # description = django_filters.CharFilter(lookup_expr='icontains')
    # status = django_filters.ChoiceFilter(choices=(('', 'all'),) + Outcome.STATUS_CHOICES)
    # scope = django_filters.ChoiceFilter(choices=(('', 'all'),) + SCOPE_CHOICES)
    # ESTIMATE_CHOICES = (
    #     ('1d', 'hour(s)'),
    #     ('1w', 'day(s)'),
    #     ('1M', 'week(s)'),
    #     ('12M', 'month(s)'),
    #     ('0m', 'unestimated'),
    # )
    # estimate = django_filters.ChoiceFilter(choices=(('', 'all'),) + ESTIMATE_CHOICES, method=filter_estimate)
    search = django_filters.CharFilter(method='search_filter', label='Text search')
    tags = django_filters.CharFilter(method='tags_filter')
    open = django_filters.BooleanFilter(method='open_filter')
    closed = django_filters.BooleanFilter(method='closed_filter')
    order_by = django_filters.OrderingFilter(
        fields=(
            ('modified', 'modified'),
            ('score', 'score'),
        )
    )

    class Meta:
        model = Outcome
        fields = {
            'name': ['exact', 'icontains', 'istartswith'],
            'status': ['exact'],
            'scope': ['exact'],
            'inbox': ['exact'],
            'date': ['exact', 'lt', 'gt', 'lte', 'gte'],
            'deadline': ['exact', 'lt', 'gt', 'lte', 'gte'],
            'estimate': ['exact'],
            'description': ['icontains'],
            'completed_at': ['exact', 'lt', 'gt', 'lte', 'gte'],
            'score': ['exact', 'lt', 'gt', 'lte', 'gte'],
            'comparisons': ['exact', 'lt', 'gt', 'lte', 'gte'],
        }

    def search_filter(self, queryset, name, value):
        return queryset.search(value)

    def open_filter(self, queryset, name, value):
        if value:
            return queryset.open()
        else:
            return queryset.closed()

    def closed_filter(self, queryset, name, value):
        if value:
            return queryset.closed()
        else:
            return queryset.open()

    def tags_filter(self, queryset, name, value):
        for id in value.split(','):
            _type, id = from_global_id(id)
            queryset = queryset.filter(tags__id__exact=id)
        return queryset


class StepFilter(django_filters.FilterSet):
    class Meta:
        model = Step
        fields = {
            'name': ['exact', 'icontains', 'istartswith'],
            'completed_at': ['exact', 'lt', 'gt', 'lte', 'gte'],
            'order': ['exact'],
        }
