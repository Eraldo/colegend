from enum import Enum

import graphene
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import Focus


class Scope(Enum):
    DAY = 'day'
    WEEK = 'week'
    MONTH = 'month'
    YEAR = 'year'


ScopeType = graphene.Enum.from_enum(Scope)


class FocusNode(DjangoObjectType):
    class Meta:
        model = Focus
        filter_fields = {
            'scope': ['exact'],
            'start': ['exact', 'lt', 'gt'],
            'end': ['exact', 'lt', 'gt'],
        }
        interfaces = [graphene.Node]


class FocusQuery(graphene.ObjectType):
    focus = graphene.Node.Field(FocusNode)
    focuses = DjangoFilterConnectionField(FocusNode)
