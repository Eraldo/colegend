import graphene
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import Checkpoint


class CheckpointNode(DjangoObjectType):
    class Meta:
        model = Checkpoint
        filter_fields = {
            'name': ['exact', 'istartswith', 'icontains'],
        }
        interfaces = [graphene.Node]


class CheckpointQuery(graphene.ObjectType):
    checkpoint = graphene.Node.Field(CheckpointNode)
    checkpoints = DjangoFilterConnectionField(CheckpointNode)
    has_checkpoint = graphene.Boolean(name=graphene.String())
    has_checkpoints = graphene.Boolean(names=graphene.String())

    def resolve_has_checkpoint(self, info, name):
        user = info.context.user
        return user.has_checkpoint(name=name)

    def resolve_has_checkpoints(self, info, names):
        user = info.context.user
        checkpoints = [name.strip() for name in names.split(',')]
        for checkpoint in checkpoints:
            if not user.has_checkpoint(checkpoint):
                return False
        return True


class AddCheckpoint(graphene.relay.ClientIDMutation):
    checkpoint = graphene.Field(CheckpointNode)

    class Input:
        name = graphene.String()

    @classmethod
    def mutate_and_get_payload(cls, root, info, name):
        user = info.context.user
        checkpoint = user.add_checkpoint(name)
        return AddCheckpoint(checkpoint=checkpoint)


class CheckpointMutation(graphene.ObjectType):
    add_checkpoint = AddCheckpoint.Field()
