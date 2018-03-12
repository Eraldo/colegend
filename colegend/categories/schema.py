import graphene
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import Category


class CategoryNode(DjangoObjectType):
    class Meta:
        model = Category
        filter_fields = {
            'name': ['exact', 'istartswith', 'icontains'],
        }
        interfaces = [graphene.Node]


class CategoryQuery(graphene.ObjectType):
    category = graphene.Node.Field(CategoryNode)
    categories = DjangoFilterConnectionField(CategoryNode)
