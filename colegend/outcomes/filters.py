import django_filters

from .models import Outcome


class OutcomeFilter(django_filters.FilterSet):
    status = django_filters.ChoiceFilter(choices=(('', 'all'),) + Outcome.STATUS_CHOICES)
    review = django_filters.ChoiceFilter(choices=(('', 'all'),) + Outcome.REVIEW_CHOICES)

    class Meta:
        model = Outcome
        fields = {
            'name': ['icontains'],
            'status': ['exact'],
            'review': ['exact'],
            'inbox': ['exact'],
        }
