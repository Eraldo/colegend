import graphene
from graphene_django.debug import DjangoDebug

from colegend.checkpoints.schema import CheckpointQuery, CheckpointMutation
from colegend.community.schema import CommunityQuery, CommunityMutation
from colegend.events.schema import EventQuery, EventMutation
from colegend.home.schema import HomeQuery, HomeMutation
from colegend.journey.schema import JourneyQuery, JourneyMutation
from colegend.metrics.schema import MetricsQuery
from colegend.outcomes.schema import OutcomeQuery
from colegend.office.schema import OfficeQuery, OfficeMutation
from colegend.studio.schema import StudioQuery, StudioMutation
from colegend.users.schema import UserQuery, UserMutation


class Query(
    UserQuery,
    CheckpointQuery,
    HomeQuery,
    StudioQuery,
    OfficeQuery,
    CommunityQuery,
    JourneyQuery,
    OutcomeQuery,
    MetricsQuery,
    EventQuery,
    graphene.ObjectType):
    debug = graphene.Field(DjangoDebug, name='__debug')


class Mutation(
    UserMutation,
    CheckpointMutation,
    HomeMutation,
    OfficeMutation,
    StudioMutation,
    JourneyMutation,
    CommunityMutation,
    EventMutation,
    graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
