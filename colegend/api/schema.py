import graphene
from graphene_django.debug import DjangoDebug

import colegend.users.schema
import colegend.office.schema
import colegend.outcomes.schema
from colegend.checkpoints.schema import CheckpointQuery, CheckpointMutation
from colegend.journey.schema import HeroQuery, HeroMutation


class Query(
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    colegend.users.schema.UserQuery,
    CheckpointQuery,
    HeroQuery,
    colegend.office.schema.FocusQuery,
    colegend.outcomes.schema.OutcomeQuery,
    graphene.ObjectType):
    debug = graphene.Field(DjangoDebug, name='__debug')


class Mutation(
    colegend.users.schema.UserMutation,
    CheckpointMutation,
    HeroMutation,
    graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
