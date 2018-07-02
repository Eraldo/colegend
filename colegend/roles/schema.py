import graphene
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphql_relay import from_global_id

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
            'kind': ['exact', 'icontains'],
        }
        interfaces = [graphene.Node]

    def resolve_icon(self, info):
        if not self.icon:
            return ''
        url = self.icon.url
        return info.context.build_absolute_uri(url)

    def resolve_strategy(self, info):
        """
        Limiting permission to admins and role energizers.
        :param info:
        :return:
        """
        user = info.context.user
        if user.is_superuser or user in self.users.all():
            return self.strategy
        else:
            return ''

    def resolve_history(self, info):
        """
        Limiting permission to admins and role energizers.
        :param info:
        :return:
        """
        user = info.context.user
        if user.is_superuser or user in self.users.all():
            return self.history
        else:
            return ''

    def resolve_notes(self, info):
        """
        Limiting permission to admins and role energizers.
        :param info:
        :return:
        """
        user = info.context.user
        if user.is_superuser or user in self.users.all():
            return self.notes
        else:
            return ''

    def resolve_checklists(self, info):
        """
        Limiting permission to admins and role energizers.
        :param info:
        :return:
        """
        user = info.context.user
        if user.is_superuser or user in self.users.all():
            return self.checklists
        else:
            return ''

    def resolve_metrics(self, info):
        """
        Limiting permission to admins and role energizers.
        :param info:
        :return:
        """
        user = info.context.user
        if user.is_superuser or user in self.users.all():
            return self.metrics
        else:
            return ''


class RoleQuery(graphene.ObjectType):
    role = graphene.Node.Field(RoleNode)
    roles = DjangoFilterConnectionField(RoleNode)


class UpdateRoleMutation(graphene.relay.ClientIDMutation):
    success = graphene.Boolean()
    role = graphene.Field(RoleNode)

    class Input:
        id = graphene.ID()
        name = graphene.String()
        nickname = graphene.String()
        item = graphene.String()
        purpose = graphene.String()
        strategy = graphene.String()
        powers = graphene.String()
        services = graphene.String()
        policies = graphene.String()
        history = graphene.String()
        notes = graphene.String()
        checklists = graphene.String()
        metrics = graphene.String()

    @classmethod
    def mutate_and_get_payload(cls, root, info, id, **kwargs):
        user = info.context.user
        if not user.is_superuser:
            raise Exception('Permission denied.')
        _type, id = from_global_id(id)
        role = Role.objects.get(id=id)
        for key, value in kwargs.items():
            if value is not None:
                setattr(role, key, value)
        role.save()
        return UpdateRoleMutation(success=True, role=role)


class RoleMutation(graphene.ObjectType):
    update_role = UpdateRoleMutation.Field()
