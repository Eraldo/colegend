import django_filters

from .models import User


class UserFilter(django_filters.FilterSet):
    class Meta:
        model = User
        fields = {
            'name': ['exact', 'icontains', 'istartswith'],
        }

