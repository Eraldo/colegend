import graphene
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import Role


class RoleNode(DjangoObjectType):
    class Meta:
        model = Role
        filter_fields = {
            'name': ['exact', 'istartswith', 'icontains'],
            'nickname': ['exact', 'istartswith', 'icontains'],
            'item': ['exact', 'istartswith', 'icontains'],
            'description': ['exact', 'icontains'],
            'metrics': ['exact', 'icontains'],

        }
        interfaces = [graphene.Node]

    def resolve_icon(self, info):
        if not self.icon:
            return ''
        url = self.icon.url
        return info.context.build_absolute_uri(url)


class RoleQuery(graphene.ObjectType):
    role = graphene.Node.Field(RoleNode)
    roles = DjangoFilterConnectionField(RoleNode)


class RoleMutation(graphene.ObjectType):
    pass
