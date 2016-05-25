import django_filters

from .models import Outcome


class OutcomeFilter(django_filters.FilterSet):
    class Meta:
        model = Outcome
        fields = ['name', 'status', 'review', 'inbox']
