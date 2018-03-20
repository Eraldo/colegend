import django_filters

from colegend.core.filters import SearchFilter
from colegend.journals.models import JournalEntry
from colegend.tags.schema import TagsFilter


class JournalEntryFilter(django_filters.FilterSet):
    search = SearchFilter()
    tags = TagsFilter()

    class Meta:
        model = JournalEntry
        fields = {
            'scope': ['exact'],
            'start': ['exact', 'lt', 'gt', 'lte', 'gte'],
            'content': ['icontains'],
            'keywords': ['exact', 'icontains', 'istartswith'],
        }
