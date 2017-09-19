from django_filters import FilterSet

from .models import Focus


class FocusFilter(FilterSet):
    class Meta:
        model = Focus
        fields = {
            'scope': ['exact'],
            'start': ['exact', 'lt', 'gt', 'lte', 'gte'],
            'end': ['exact', 'lt', 'gt', 'lte', 'gte'],
        }
