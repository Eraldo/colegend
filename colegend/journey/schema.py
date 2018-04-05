import graphene
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphql_relay import from_global_id

from .models import Hero, Demon, Quote


class HeroNode(DjangoObjectType):
    class Meta:
        model = Hero
        filter_fields = {
            'content': ['icontains'],
        }
        interfaces = [graphene.Node]


class HeroQuery(graphene.ObjectType):
    hero = graphene.Node.Field(HeroNode)
    heroes = DjangoFilterConnectionField(HeroNode)


class UpdateHero(graphene.relay.ClientIDMutation):
    success = graphene.Boolean()
    hero = graphene.Field(HeroNode)

    class Input:
        name = graphene.String()
        avatar = graphene.String()
        year_topic = graphene.String()
        vision = graphene.String()
        mission = graphene.String()
        values = graphene.String()
        powers = graphene.String()
        skills = graphene.String()
        habits = graphene.String()
        principles = graphene.String()
        wishes = graphene.String()
        goals = graphene.String()
        people = graphene.String()
        resources = graphene.String()
        achievements = graphene.String()
        questions = graphene.String()
        experiments = graphene.String()
        projects = graphene.String()
        bucket = graphene.String()
        roles = graphene.String()
        strategy = graphene.String()
        inspirations = graphene.String()
        routines = graphene.String()
        blueprint_day = graphene.String()
        blueprint_week = graphene.String()
        blueprint_month = graphene.String()
        content = graphene.String()

    @classmethod
    def mutate_and_get_payload(cls, root, info, **kwargs):
        user = info.context.user
        hero = user.hero
        for key, value in kwargs.items():
            if value is not None:
                setattr(hero, key, value)
        hero.save()
        return UpdateHero(success=True, hero=hero)


class HeroMutation(graphene.ObjectType):
    update_hero = UpdateHero.Field()


class DemonNode(DjangoObjectType):
    class Meta:
        model = Demon
        filter_fields = {
            'content': ['icontains'],
        }
        interfaces = [graphene.Node]


class DemonQuery(graphene.ObjectType):
    demon = graphene.Node.Field(DemonNode)
    demons = DjangoFilterConnectionField(DemonNode)


class UpdateDemon(graphene.relay.ClientIDMutation):
    success = graphene.Boolean()
    demon = graphene.Field(DemonNode)

    class Input:
        name = graphene.String()
        avatar = graphene.String()
        tensions = graphene.String()
        fears = graphene.String()
        content = graphene.String()

    @classmethod
    def mutate_and_get_payload(cls, root, info, **kwargs):
        user = info.context.user
        demon = user.demon
        for key, value in kwargs.items():
            if value is not None:
                setattr(demon, key, value)
        demon.save()
        return UpdateDemon(success=True, demon=demon)


class DemonMutation(graphene.ObjectType):
    update_demon = UpdateDemon.Field()


class QuoteNode(DjangoObjectType):
    liked = graphene.Field(
        graphene.Boolean
    )
    disliked = graphene.Field(
        graphene.Boolean
    )

    class Meta:
        model = Quote
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
            'content': ['exact', 'icontains', 'istartswith'],
            'author': ['exact', 'icontains', 'istartswith'],
            'categories': ['exact'],
            'accepted': ['exact'],
            'used_as_daily': ['exact', 'lt', 'gt', 'lte', 'gte'],
        }
        interfaces = [graphene.Node]

    def resolve_liked(self, info):
        user = info.context.user
        return user.liked_quotes.filter(id=self.id).exists()

    def resolve_disliked(self, info):
        user = info.context.user
        return user.disliked_quotes.filter(id=self.id).exists()


class QuoteQuery(graphene.ObjectType):
    quote = graphene.Node.Field(QuoteNode)
    quotes = DjangoFilterConnectionField(QuoteNode)
    daily_quote = graphene.Field(QuoteNode)

    def resolve_daily_quote(self, info):
        return Quote.objects.daily_quote()
#
#
# class FeedbackQuoteMutation(graphene.relay.ClientIDMutation):
#     success = graphene.Boolean()
#     quote = graphene.Field(QuoteNode)
#
#     class Input:
#         id = graphene.ID()
#         liked = graphene.Boolean()
#         disliked = graphene.Boolean()
#
#     @classmethod
#     def mutate_and_get_payload(cls, root, info, id, liked=None, disliked=None):
#         user = info.context.user
#         _type, id = from_global_id(id)
#         quote = Quote.objects.get(id=id)
#
#         # Make sure either liked or disliked was selected.
#         if liked is None and disliked is None:
#             raise Exception('Please provide feedback.')
#         if liked is not None and disliked is not None:
#             raise Exception('Please either like or dislike.')
#
#         if liked is not None:
#             quote.like(user)
#         elif disliked is not None:
#             quote.dislike(user)
#
#         return FeedbackQuoteMutation(success=True, quote=quote)


class LikeQuoteMutation(graphene.relay.ClientIDMutation):
    success = graphene.Boolean()
    quote = graphene.Field(QuoteNode)

    class Input:
        id = graphene.ID()

    @classmethod
    def mutate_and_get_payload(cls, root, info, id):
        user = info.context.user
        _type, id = from_global_id(id)
        quote = Quote.objects.get(id=id)
        quote.like(user)
        return LikeQuoteMutation(success=True, quote=quote)


class DislikeQuoteMutation(graphene.relay.ClientIDMutation):
    success = graphene.Boolean()
    quote = graphene.Field(QuoteNode)

    class Input:
        id = graphene.ID()

    @classmethod
    def mutate_and_get_payload(cls, root, info, id):
        user = info.context.user
        _type, id = from_global_id(id)
        quote = Quote.objects.get(id=id)
        quote.dislike(user)
        return DislikeQuoteMutation(success=True, quote=quote)


class QuoteMutation(graphene.ObjectType):
    like_quote = LikeQuoteMutation.Field()
    dislike_quote = DislikeQuoteMutation.Field()


class JourneyQuery(
    HeroQuery,
    DemonQuery,
    QuoteQuery,
    graphene.ObjectType):
    pass


class JourneyMutation(
    HeroMutation,
    DemonMutation,
    QuoteMutation,
    graphene.ObjectType):
    pass
