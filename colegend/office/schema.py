import graphene
from graphene_django import DjangoObjectType

from .models import Focus


class FocusType(DjangoObjectType):
    class Meta:
        model = Focus


class Query(graphene.AbstractType):
    focus = graphene.Field(
        FocusType,
        id=graphene.Int(),
    )
    all_focuses = graphene.List(FocusType)

    def resolve_all_focuses(self, args, context, info):
        return Focus.objects.all()

    def resolve_focus(self, args, context, info):
        id = args.get('id')

        if id is not None:
            return Focus.objects.get(id=id)

        return None
