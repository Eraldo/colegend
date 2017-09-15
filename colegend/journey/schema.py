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
        content = graphene.String()

    @classmethod
    def mutate_and_get_payload(cls, root, info, content):
        user = info.context.user
        hero = user.hero
        hero.content = content
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
        content = graphene.String()

    @classmethod
    def mutate_and_get_payload(cls, root, info, content):
        user = info.context.user
        demon = user.demon
        demon.content = content
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
