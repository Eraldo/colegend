import graphene
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import Outcome


class OutcomeType(DjangoObjectType):
    class Meta:
        model = Outcome
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
        }
        interfaces = [graphene.Node]


class Query(graphene.ObjectType):
    outcome = graphene.Node.Field(OutcomeType)
    outcomes = DjangoFilterConnectionField(OutcomeType)
