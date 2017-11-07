import graphene
from django.utils import timezone
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import Tutorial


class TutorialNode(DjangoObjectType):
    class Meta:
        model = Tutorial
        filter_fields = {
            'name': ['exact', 'istartswith', 'icontains'],
            'content': ['exact', 'icontains'],
        }
        interfaces = [graphene.Node]


class TutorialQuery(graphene.ObjectType):
    # tutorial = graphene.Node.Field(TutorialNode)
    tutorial = graphene.Field(TutorialNode, name=graphene.String())
    tutorials = DjangoFilterConnectionField(TutorialNode)

    def resolve_tutorial(self, info, name):
        return Tutorial.objects.get(name__iexact=name)


class TutorialMutation(graphene.ObjectType):
    pass
