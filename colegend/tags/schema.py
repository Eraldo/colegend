import django_filters
import graphene
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphql_relay import from_global_id

from colegend.api.models import CountableConnectionBase
from .models import Tag


class TagsFilter(django_filters.BaseCSVFilter, django_filters.CharFilter):
    def filter(self, queryset, value):
        # value is either a list or an 'empty' value
        values = value or []

        for value in values:
            _type, id = from_global_id(value)
            queryset = queryset.filter(tags__id__exact=id)
        return queryset


class TagNode(DjangoObjectType):
    class Meta:
        model = Tag
        filter_fields = {
            'name': ['exact', 'istartswith', 'icontains'],
            'description': ['exact', 'icontains'],
            'owner': ['exact'],
        }
        interfaces = [graphene.Node]
        connection_class = CountableConnectionBase


class TagQuery(graphene.ObjectType):
    tag = graphene.Node.Field(TagNode)
    tags = DjangoFilterConnectionField(TagNode)


class CreateTagMutation(graphene.relay.ClientIDMutation):
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
        return CreateTagMutation(success=True, tag=tag)


class UpdateTagMutation(graphene.relay.ClientIDMutation):
    success = graphene.Boolean()
    tag = graphene.Field(TagNode)

    class Input:
        id = graphene.ID()
        name = graphene.String()
        description = graphene.String()

    @classmethod
    def mutate_and_get_payload(cls, root, info, id, name=None, description=None):
        user = info.context.user
        _type, id = from_global_id(id)
        tag = user.tags.get(id=id)
        if name is not None:
            tag.name = name
        if description is not None:
            tag.description = description
        tag.save()
        return UpdateTagMutation(success=True, tag=tag)


class DeleteTagMutation(graphene.relay.ClientIDMutation):
    success = graphene.Boolean()

    class Input:
        id = graphene.ID()

    @classmethod
    def mutate_and_get_payload(cls, root, info, id):
        user = info.context.user
        _type, id = from_global_id(id)
        tag = user.tags.get(id=id)
        tag.delete()
        return DeleteTagMutation(success=True)


class TagMutation(graphene.ObjectType):
    create_tag = CreateTagMutation.Field()
    update_tag = UpdateTagMutation.Field()
    delete_tag = DeleteTagMutation.Field()
