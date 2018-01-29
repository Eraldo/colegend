import graphene
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import Hero, Demon


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
    demones = DjangoFilterConnectionField(DemonNode)


class UpdateDemon(graphene.relay.ClientIDMutation):
    success = graphene.Boolean()
    demon = graphene.Field(DemonNode)

    class Input:
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


class JourneyQuery(
    HeroQuery,
    DemonQuery,
    graphene.ObjectType):
    pass


class JourneyMutation(
    HeroMutation,
    DemonMutation,
    graphene.ObjectType):
    pass
