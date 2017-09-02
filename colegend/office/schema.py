import graphene
from graphene_django import DjangoObjectType

from .models import Focus


class FocusType(DjangoObjectType):
    class Meta:
        model = Focus


class FocusQuery(graphene.ObjectType):
    focus = graphene.Field(
        FocusType,
        id=graphene.Int(),
    )
    focuses = graphene.List(FocusType)

    def resolve_focuses(self, info):
        return Focus.objects.all()

    def resolve_focus(self, info, id=None):
        if id is not None:
            return Focus.objects.get(id=id)
        return None
