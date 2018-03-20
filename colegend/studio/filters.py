import django_filters

from colegend.journals.models import JournalEntry
from colegend.tags.schema import TagsFilter


class JournalEntryFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(method='search_filter', label='Text search')
    tags = TagsFilter()

    class Meta:
        model = JournalEntry
        fields = {
            'scope': ['exact'],
            'start': ['exact', 'lt', 'gt', 'lte', 'gte'],
            'content': ['icontains'],
            'keywords': ['exact', 'icontains', 'istartswith'],
        }

    def search_filter(self, queryset, name, value):
        return queryset.search(value)
