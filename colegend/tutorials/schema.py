import graphene
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
    tutorial = graphene.Node.Field(TutorialNode)
    tutorial_by_name = graphene.Field(TutorialNode, name=graphene.String())
    tutorials = DjangoFilterConnectionField(TutorialNode)

    def resolve_tutorial_by_name(self, info, name):
        try:
            return Tutorial.objects.get(name__iexact=name)
        except Tutorial.DoesNotExist:
            return None


class TutorialMutation(graphene.ObjectType):
    pass
