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
