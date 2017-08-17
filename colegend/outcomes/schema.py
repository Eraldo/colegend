import graphene
from graphene_django import DjangoObjectType

from .models import Outcome


class OutcomeType(DjangoObjectType):
    class Meta:
        model = Outcome


class Query(graphene.AbstractType):
    outcome = graphene.Field(
        OutcomeType,
        id=graphene.Int(),
        name=graphene.String(),
    )
    all_outcomes = graphene.List(OutcomeType)

    def resolve_all_outcomes(self, args, context, info):
        return Outcome.objects.all()
