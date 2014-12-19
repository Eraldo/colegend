import factory
from tags.models import Tag
from users.tests.test_models import UserFactory

__author__ = 'eraldo'


class TagFactory(factory.DjangoModelFactory):

    class Meta:
        model = Tag
        django_get_or_create = ('name',)

    owner = factory.SubFactory(UserFactory)
    name = factory.Sequence(lambda n: 'Tag{0}'.format(n))
    description = "Some description."
