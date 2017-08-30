import graphene
from graphene_django import DjangoObjectType

from .models import Outcome


class OutcomeType(DjangoObjectType):
    class Meta:
        model = Outcome


class Query(graphene.ObjectType):
    outcome = graphene.Field(
        OutcomeType,
        id=graphene.Int(),
        name=graphene.String(),
    )
    outcomes = graphene.List(OutcomeType)

    def resolve_outcomes(self, info):
        return Outcome.objects.all()

    def resolve_outcome(self, info, id=None, name=None):
        if id is not None:
            return Outcome.objects.get(id=id)
        if name is not None:
            return Outcome.objects.get(name=name)
        return None

