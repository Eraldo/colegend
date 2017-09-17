import graphene
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from colegend.outcomes.schema import OutcomeQuery, OutcomeMutation
from .models import Focus


class FocusNode(DjangoObjectType):
    class Meta:
        model = Focus
        filter_fields = {
            'scope': ['exact'],
            'start': ['exact', 'lt', 'gt', 'lte', 'gte'],
            'end': ['exact', 'lt', 'gt', 'lte', 'gte'],
        }
        interfaces = [graphene.Node]


class FocusQuery(graphene.ObjectType):
    focus = graphene.Node.Field(FocusNode)
    focuses = DjangoFilterConnectionField(FocusNode)


class OfficeQuery(
    OutcomeQuery,
    FocusQuery,
    graphene.ObjectType):
    pass


class OfficeMutation(
    OutcomeMutation,
    graphene.ObjectType):
    pass
