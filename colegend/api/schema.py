import graphene
from graphene_django.debug import DjangoDebug

from colegend.academy.schema import AcademyQuery, AcademyMutation
from colegend.arcade.schema import ArcadeQuery, ArcadeMutation
from colegend.categories.schema import CategoryQuery
from colegend.checkpoints.schema import CheckpointQuery, CheckpointMutation
from colegend.community.schema import CommunityQuery, CommunityMutation
from colegend.events.schema import EventQuery, EventMutation
from colegend.home.schema import HomeQuery, HomeMutation
from colegend.journey.schema import JourneyQuery, JourneyMutation
from colegend.metrics.schema import MetricsQuery
from colegend.news.schema import NewsQuery, NewsMutation
from colegend.office.schema import OfficeQuery, OfficeMutation
from colegend.roles.schema import RoleQuery, RoleMutation
from colegend.studio.schema import StudioQuery, StudioMutation
from colegend.tags.schema import TagQuery, TagMutation
from colegend.tutorials.schema import TutorialQuery, TutorialMutation
from colegend.users.schema import UserQuery, UserMutation


class Query(
    UserQuery,
    CheckpointQuery,
    HomeQuery,
    ArcadeQuery,
    StudioQuery,
    OfficeQuery,
    CommunityQuery,
    AcademyQuery,
    JourneyQuery,
    MetricsQuery,
    EventQuery,
    NewsQuery,
    RoleQuery,
    TutorialQuery,
    TagQuery,
    CategoryQuery,
    graphene.ObjectType):
    debug = graphene.Field(DjangoDebug, name='__debug')


class Mutation(
    UserMutation,
    CheckpointMutation,
    HomeMutation,
    ArcadeMutation,
    OfficeMutation,
    StudioMutation,
    CommunityMutation,
    AcademyMutation,
    JourneyMutation,
    EventMutation,
    NewsMutation,
    RoleMutation,
    TutorialMutation,
    TagMutation,
    graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
