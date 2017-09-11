import graphene
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import Hero


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
