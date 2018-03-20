import django_filters


class SearchFilter(django_filters.CharFilter):
    def filter(self, queryset, value):
        return queryset.search(value)
