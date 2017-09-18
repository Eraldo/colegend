import graphene
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphql_relay import from_global_id

from colegend.office.types import StatusType
from colegend.outcomes.filters import OutcomeFilter
from colegend.scopes.schema import ScopeType
from .models import Outcome


class OutcomeNode(DjangoObjectType):
    class Meta:
        model = Outcome
        interfaces = [graphene.Node]


class OutcomeQuery(graphene.ObjectType):
    outcome = graphene.Node.Field(OutcomeNode)
    outcomes = DjangoFilterConnectionField(OutcomeNode, filterset_class=OutcomeFilter)


class CreateOutcomeMutation(graphene.relay.ClientIDMutation):
    success = graphene.Boolean()
    outcome = graphene.Field(OutcomeNode)

    class Input:
        name = graphene.String()
        description = graphene.String()
        status = StatusType()
        inbox = graphene.Boolean()
        scope = ScopeType()
        date = graphene.types.datetime.DateTime()
        deadline = graphene.types.datetime.DateTime()
        estimate = graphene.String()

    @classmethod
    def mutate_and_get_payload(cls, root, info, **kwargs):
        user = info.context.user
        outcome = user.outcomes.create(**kwargs)
        return CreateOutcomeMutation(success=True, outcome=outcome)


class UpdateOutcomeMutation(graphene.relay.ClientIDMutation):
    success = graphene.Boolean()
    outcome = graphene.Field(OutcomeNode)

    class Input:
        id = graphene.ID()
        name = graphene.String()
        description = graphene.String()
        status = StatusType()
        inbox = graphene.Boolean()
        scope = ScopeType()
        date = graphene.types.datetime.DateTime()
        deadline = graphene.types.datetime.DateTime()
        estimate = graphene.String()

    @classmethod
    def mutate_and_get_payload(
        cls, root, info, id,
        name=None, description=None, status=None, inbox=None,
        scope=None, date=None, deadline=None, estimate=None):
        user = info.context.user
        _type, id = from_global_id(id)
        # TODO: Checking permission. Workaround: Only my outcomes. ;)
        outcome = user.outcomes.get(id=id)
        if name is not None:
            outcome.name = name
        if description is not None:
            outcome.description = description
        if status is not None:
            outcome.status = status
        if inbox is not None:
            outcome.inbox = inbox
        if scope is not None:
            outcome.scope = scope
        if date is not None:
            outcome.date = date
        if deadline is not None:
            outcome.deadline = deadline
        if estimate is not None:
            outcome.estimate = estimate
        outcome.save()
        return UpdateOutcomeMutation(success=True, outcome=outcome)


class DeleteOutcomeMutation(graphene.relay.ClientIDMutation):
    success = graphene.Boolean()

    class Input:
        id = graphene.ID()

    @classmethod
    def mutate_and_get_payload(cls, root, info, id):
        user = info.context.user
        _type, id = from_global_id(id)
        # TODO: Checking permission. Workaround: Only my outcomes. ;)
        outcome = user.outcomes.get(id=id)
        if outcome.is_focus:
            raise Exception('This outcome is set as a focus and cannot be deleted.')
        outcome.delete()
        return DeleteOutcomeMutation(success=True)


class OutcomeMutation(graphene.ObjectType):
    create_outcome = CreateOutcomeMutation.Field()
    update_outcome = UpdateOutcomeMutation.Field()
    delete_outcome = DeleteOutcomeMutation.Field()
