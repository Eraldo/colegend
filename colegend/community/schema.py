import graphene
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphql_relay import from_global_id

from .models import Duo, Clan, Tribe


class DuoNode(DjangoObjectType):
    is_open = graphene.Field(
        graphene.Boolean,
    )

    class Meta:
        model = Duo
        filter_fields = {
            'name': ['exact', 'istartswith', 'icontains'],
        }
        interfaces = [graphene.Node]

    def resolve_is_open(self, info):
        return self.is_open


class DuoQuery(graphene.ObjectType):
    duo = graphene.Node.Field(DuoNode)
    duos = DjangoFilterConnectionField(DuoNode)


class UpdateDuoMutation(graphene.relay.ClientIDMutation):
    duo = graphene.Field(DuoNode)

    class Input:
        id = graphene.ID()
        name = graphene.String()
        notes = graphene.String()

    @classmethod
    def mutate_and_get_payload(cls, root, info, id, name=None, notes=None):
        _type, id = from_global_id(id)
        duo = Duo.objects.get(id=id)
        if name is not None:
            duo.name = name
        if notes is not None:
            duo.notes = notes
        duo.save()
        return UpdateDuoMutation(duo=duo)


class JoinDuoMutation(graphene.relay.ClientIDMutation):
    duo = graphene.Field(DuoNode)

    class Input:
        id = graphene.ID()

    @classmethod
    def mutate_and_get_payload(cls, root, info, id):
        user = info.context.user
        _type, id = from_global_id(id)
        duo = Duo.objects.get(id=id)
        duo.join(user)
        return JoinDuoMutation(duo=duo)


class QuitDuoMutation(graphene.relay.ClientIDMutation):
    duo = graphene.Field(DuoNode)

    class Input:
        pass

    @classmethod
    def mutate_and_get_payload(cls, root, info):
        user = info.context.user
        duo = user.duo
        duo.quit(user)
        return QuitDuoMutation(duo=duo)


class AddDuoMutation(graphene.relay.ClientIDMutation):
    duo = graphene.Field(DuoNode)

    class Input:
        name = graphene.String()

    @classmethod
    def mutate_and_get_payload(cls, root, info, name):
        user = info.context.user
        duo, created = Duo.objects.get_or_create(name=name)
        duo.join(user)
        return AddDuoMutation(duo=duo)


class DuoMutation(graphene.ObjectType):
    update_duo = UpdateDuoMutation.Field()
    add_duo = AddDuoMutation.Field()
    join_duo = JoinDuoMutation.Field()
    quit_duo = QuitDuoMutation.Field()


class ClanNode(DjangoObjectType):
    is_open = graphene.Field(
        graphene.Boolean,
    )

    class Meta:
        model = Clan
        filter_fields = {
            'name': ['exact', 'istartswith', 'icontains'],
        }
        interfaces = [graphene.Node]

    def resolve_is_open(self, info):
        return self.is_open


class ClanQuery(graphene.ObjectType):
    clan = graphene.Node.Field(ClanNode)
    clans = DjangoFilterConnectionField(ClanNode)


class UpdateClanMutation(graphene.relay.ClientIDMutation):
    clan = graphene.Field(ClanNode)

    class Input:
        id = graphene.ID()
        name = graphene.String()
        notes = graphene.String()

    @classmethod
    def mutate_and_get_payload(cls, root, info, id, name=None, notes=None):
        _type, id = from_global_id(id)
        clan = Clan.objects.get(id=id)
        if name is not None:
            clan.name = name
        if notes is not None:
            clan.notes = notes
        clan.save()
        return UpdateClanMutation(clan=clan)


class JoinClanMutation(graphene.relay.ClientIDMutation):
    clan = graphene.Field(ClanNode)

    class Input:
        id = graphene.ID()

    @classmethod
    def mutate_and_get_payload(cls, root, info, id):
        user = info.context.user
        _type, id = from_global_id(id)
        clan = Clan.objects.get(id=id)
        clan.join(user)
        return JoinClanMutation(clan=clan)


class QuitClanMutation(graphene.relay.ClientIDMutation):
    clan = graphene.Field(ClanNode)

    class Input:
        pass

    @classmethod
    def mutate_and_get_payload(cls, root, info):
        user = info.context.user
        clan = user.clan
        clan.quit(user)
        return QuitClanMutation(clan=clan)


class AddClanMutation(graphene.relay.ClientIDMutation):
    clan = graphene.Field(ClanNode)

    class Input:
        name = graphene.String()

    @classmethod
    def mutate_and_get_payload(cls, root, info, name):
        user = info.context.user
        clan, created = Clan.objects.get_or_create(name=name)
        clan.join(user)
        return AddClanMutation(clan=clan)


class ClanMutation(graphene.ObjectType):
    update_clan = UpdateClanMutation.Field()
    add_clan = AddClanMutation.Field()
    join_clan = JoinClanMutation.Field()
    quit_clan = QuitClanMutation.Field()


class TribeNode(DjangoObjectType):
    is_open = graphene.Field(
        graphene.Boolean,
    )

    class Meta:
        model = Tribe
        filter_fields = {
            'name': ['exact', 'istartswith', 'icontains'],
        }
        interfaces = [graphene.Node]

    def resolve_is_open(self, info):
        return self.is_open


class TribeQuery(graphene.ObjectType):
    tribe = graphene.Node.Field(TribeNode)
    tribes = DjangoFilterConnectionField(TribeNode)


class JoinTribeMutation(graphene.relay.ClientIDMutation):
    tribe = graphene.Field(TribeNode)

    class Input:
        id = graphene.ID()

    @classmethod
    def mutate_and_get_payload(cls, root, info, id):
        user = info.context.user
        _type, id = from_global_id(id)
        tribe = Tribe.objects.get(id=id)
        tribe.join(user)
        return JoinTribeMutation(tribe=tribe)


class QuitTribeMutation(graphene.relay.ClientIDMutation):
    tribe = graphene.Field(TribeNode)

    class Input:
        pass

    @classmethod
    def mutate_and_get_payload(cls, root, info):
        user = info.context.user
        tribe = user.tribe
        tribe.quit(user)
        return QuitTribeMutation(tribe=tribe)


class AddTribeMutation(graphene.relay.ClientIDMutation):
    tribe = graphene.Field(TribeNode)

    class Input:
        name = graphene.String()

    @classmethod
    def mutate_and_get_payload(cls, root, info, name):
        user = info.context.user
        tribe, created = Tribe.objects.get_or_create(name=name)
        tribe.join(user)
        return AddTribeMutation(tribe=tribe)


class TribeMutation(graphene.ObjectType):
    add_tribe = AddTribeMutation.Field()
    join_tribe = JoinTribeMutation.Field()
    quit_tribe = QuitTribeMutation.Field()


class CommunityQuery(
    DuoQuery,
    ClanQuery,
    TribeQuery,
    graphene.ObjectType):
    pass


class CommunityMutation(
    DuoMutation,
    ClanMutation,
    TribeMutation,
    graphene.ObjectType):
    pass
