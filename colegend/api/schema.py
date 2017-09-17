import graphene
from graphene_django.debug import DjangoDebug

from colegend.checkpoints.schema import CheckpointQuery, CheckpointMutation
from colegend.community.schema import CommunityQuery, CommunityMutation
from colegend.home.schema import HomeQuery, HomeMutation
from colegend.journey.schema import JourneyQuery, JourneyMutation
from colegend.office.schema import FocusQuery
from colegend.outcomes.schema import OutcomeQuery
from colegend.studio.schema import StudioQuery, StudioMutation
from colegend.users.schema import UserQuery, UserMutation


class Query(
    UserQuery,
    CheckpointQuery,
    HomeQuery,
    StudioQuery,
    JourneyQuery,
    CommunityQuery,
    FocusQuery,
    OutcomeQuery,
    graphene.ObjectType):
    debug = graphene.Field(DjangoDebug, name='__debug')


class Mutation(
    UserMutation,
    CheckpointMutation,
    HomeMutation,
    StudioMutation,
    JourneyMutation,
    CommunityMutation,
    graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
