import factory
from statuses.models import Status

__author__ = 'eraldo'


class StatusFactory(factory.DjangoModelFactory):

    class Meta:
        model = Status
        django_get_or_create = ('name',)

    name = factory.Sequence(lambda n: 'Status{0}'.format(n))
    order = factory.Sequence(lambda n: n)
