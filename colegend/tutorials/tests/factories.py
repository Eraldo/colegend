import factory
from tutorials.models import Tutorial

__author__ = 'eraldo'


class TutorialFactory(factory.DjangoModelFactory):

    class Meta:
        model = Tutorial
        django_get_or_create = ('name',)

    name = factory.Sequence(lambda n: 'Tutorial{0}'.format(n))
    description = "Some description."
