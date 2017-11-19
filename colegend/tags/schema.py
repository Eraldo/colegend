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


class CreateTag(graphene.relay.ClientIDMutation):
    success = graphene.Boolean()
    tag = graphene.Field(TagNode)

    class Input:
        name = graphene.String()
        description = graphene.String()

    @classmethod
    def mutate_and_get_payload(cls, root, info, name, description=None):
        user = info.context.user
        if len(name) < 2:
            raise Exception('Please enter a tag name with at least two characters.')
        tag = user.tags.create(name=name, description=description)
        return CreateTag(success=True, tag=tag)


class DeleteTag(graphene.relay.ClientIDMutation):
    success = graphene.Boolean()

    class Input:
        id = graphene.ID()

    @classmethod
    def mutate_and_get_payload(cls, root, info, id):
        user = info.context.user
        _type, id = from_global_id(id)
        tag = user.tags.get(id=id)
        tag.delete()
        return DeleteTag(success=True)


class TagMutation(graphene.ObjectType):
    create_tag = CreateTag.Field()
    delete_tag = DeleteTag.Field()
