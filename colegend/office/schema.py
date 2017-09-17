import graphene
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

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
