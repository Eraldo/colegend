import django_filters

from .models import BlogArticlePage


class BlogArticlePageFilter(django_filters.FilterSet):
    class Meta:
        model = BlogArticlePage
        # form = BlogArticlePageFilterForm
        fields = ['tags', 'date', 'owner']
