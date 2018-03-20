import django_filters
from graphql_relay import from_global_id

from colegend.core.filters import SearchFilter
from colegend.tags.schema import TagsFilter
from .models import Adventure, AdventureReview


class AdventureFilter(django_filters.FilterSet):
    search = SearchFilter()
    tags = TagsFilter()
    completed = django_filters.BooleanFilter(method='completed_filter')

    class Meta:
        model = Adventure
        fields = {
            'name': ['exact', 'istartswith', 'icontains'],
            'scope': ['exact'],
            'public': ['exact'],
            'content': ['exact', 'icontains'],
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super().__init__(*args, **kwargs)

    def completed_filter(self, queryset, name, value):
        if value is True:
            return queryset.filter(adventurers__pk=self.user.id)
        elif value is False:
            return queryset.exclude(adventurers__pk=self.user.id)
        return queryset


class AdventureReviewFilter(django_filters.FilterSet):
    class Meta:
        model = AdventureReview
        fields = {
            'owner': ['exact'],
            'adventure': ['exact'],
            'rating': ['exact', 'lt', 'gt', 'lte', 'gte'],
            'content': ['exact', 'icontains'],
        }
