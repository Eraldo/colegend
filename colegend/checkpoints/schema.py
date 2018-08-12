import graphene
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from colegend.journey.models import QuestObjective
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
        if not user.is_authenticated:
            return False
        return user.has_checkpoint(name=name)

    def resolve_has_checkpoints(self, info, names):
        user = info.context.user
        if not user.is_authenticated:
            return False
        checkpoints = [name.strip() for name in names.split(',')]
        for checkpoint in checkpoints:
            if not user.has_checkpoint(checkpoint):
                return False
        return True


class AddCheckpointMutation(graphene.relay.ClientIDMutation):
    checkpoint = graphene.Field(CheckpointNode)

    class Input:
        name = graphene.String()

    @classmethod
    def mutate_and_get_payload(cls, root, info, name):
        user = info.context.user
        if not user.is_authenticated:
            return AddCheckpointMutation(checkpoint=Checkpoint.objects.none())
        checkpoint = user.add_checkpoint(name)
        # TODO: Fix workaround by implementing clear quest/objective completion flow/triggers.
        if checkpoint.name == 'colegend tutorial':
            # Complete associated quest objective
            quest_status = user.quest_statuses.first()
            if checkpoint and quest_status:
                objective = QuestObjective.objects.get(code='intro_watch')
                quest_status.complete_objective(objective)
        return AddCheckpointMutation(checkpoint=checkpoint)


class CheckpointMutation(graphene.ObjectType):
    add_checkpoint = AddCheckpointMutation.Field()
