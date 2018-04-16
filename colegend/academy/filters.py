import django_filters
from graphql_relay import from_global_id

from colegend.core.filters import SearchFilter
from colegend.tags.schema import TagsFilter
from .models import Book, BookReview


class BookFilter(django_filters.FilterSet):
    search = SearchFilter()
    tags = TagsFilter()
    order_by = django_filters.OrderingFilter(
        fields=(
            ('modified', 'modified'),
            ('created', 'created'),
            ('name', 'name'),
            ('author', 'author'),
            ('rating', 'rating'),
        )
    )

    class Meta:
        model = Book
        fields = {
            'name': ['exact', 'istartswith', 'icontains'],
            'author': ['exact', 'istartswith', 'icontains'],
            'content': ['exact', 'icontains'],
            'featured': ['exact'],
            'public': ['exact'],
        }


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
