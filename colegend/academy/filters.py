import django_filters

from .models import Book, BookReview


class BookFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(method='search_filter')

    class Meta:
        model = Book
        fields = {
            'name': ['exact', 'istartswith', 'icontains'],
            'author': ['exact', 'istartswith', 'icontains'],
            'content': ['exact', 'icontains'],
            'featured': ['exact'],
            'public': ['exact'],
        }

    def search_filter(self, queryset, name, value):
        return queryset.search(value)


class BookReviewFilter(django_filters.FilterSet):
    class Meta:
        model = BookReview
        fields = {
            'owner': ['exact'],
            'book': ['exact'],
            'content': ['exact', 'icontains'],
            'area_1': ['exact', 'lt', 'gt', 'lte', 'gte'],
            'area_2': ['exact', 'lt', 'gt', 'lte', 'gte'],
            'area_3': ['exact', 'lt', 'gt', 'lte', 'gte'],
            'area_4': ['exact', 'lt', 'gt', 'lte', 'gte'],
            'area_5': ['exact', 'lt', 'gt', 'lte', 'gte'],
            'area_6': ['exact', 'lt', 'gt', 'lte', 'gte'],
            'area_7': ['exact', 'lt', 'gt', 'lte', 'gte'],
        }
