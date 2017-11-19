import graphene
from django.utils import timezone
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphql_relay import from_global_id

from .models import Tag


class TagNode(DjangoObjectType):
    class Meta:
        model = Tag
        filter_fields = {
            'name': ['exact', 'istartswith', 'icontains'],
            'description': ['exact', 'icontains'],
            'owner': ['exact'],
        }
        interfaces = [graphene.Node]


class TagQuery(graphene.ObjectType):
    tag = graphene.Node.Field(TagNode)
    tags = DjangoFilterConnectionField(TagNode)


class AddTag(graphene.relay.ClientIDMutation):
    tag = graphene.Field(TagNode)

    class Input:
        name = graphene.String()
        description = graphene.String()

    @classmethod
    def mutate_and_get_payload(cls, root, info, *args, **kwargs):
        user = info.context.user
        tag = user.tags.create(*args, **kwargs)
        return AddTag(tag=tag)


class DeleteTag(graphene.relay.ClientIDMutation):
    success = graphene.Boolean()

    class Input:
        id = graphene.ID()

    @classmethod
    def mutate_and_get_payload(cls, root, info, id):
        user = info.context.user
        _type, id = from_global_id(id)
        tag = user.objects.tags.get(id=id)
        tag.delete()
        return DeleteTag(success=True)


class TagMutation(graphene.ObjectType):
    add_tag = AddTag.Field()
    delete_tag = DeleteTag.Field()
