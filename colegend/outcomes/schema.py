import graphene
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphql_relay import from_global_id

from colegend.office.types import StatusType
from colegend.scopes.schema import ScopeType
from .models import Outcome


class OutcomeNode(DjangoObjectType):
    class Meta:
        model = Outcome
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
            'status': ['exact'],
            'scope': ['exact'],
            'inbox': ['exact'],
            'date': ['exact', 'lt', 'gt', 'lte', 'gte'],
            'deadline': ['exact', 'lt', 'gt', 'lte', 'gte'],
            'estimate': ['exact'],
        }
        interfaces = [graphene.Node]


class OutcomeQuery(graphene.ObjectType):
    outcome = graphene.Node.Field(OutcomeNode)
    outcomes = DjangoFilterConnectionField(OutcomeNode)


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
        if name:
            outcome.name = name
        if description:
            outcome.description = description
        if status:
            outcome.status = status
        if inbox:
            outcome.inbox = inbox
        if scope:
            outcome.scope = scope
        if date:
            outcome.date = date
        if deadline:
            outcome.deadline = deadline
        if estimate:
            outcome.estimate = estimate
        outcome.save()
        return UpdateOutcomeMutation(success=True, outcome=outcome)


class DeleteOutcomeMutation(graphene.relay.ClientIDMutation):
    success = graphene.Boolean()
    outcome = graphene.Field(OutcomeNode)

    class Input:
        id = graphene.ID()

    @classmethod
    def mutate_and_get_payload(cls, root, info, id):
        user = info.context.user
        _type, id = from_global_id(id)
        # TODO: Checking permission. Workaround: Only my outcomes. ;)
        outcome = user.outcomes.get(id=id)
        if outcome.is_focus:
            raise Exception('This outcome is set as a focus and can only be set to done canceled.')
        outcome.delete()
        return DeleteOutcomeMutation(success=True, outcome=outcome)


class OutcomeMutation(graphene.ObjectType):
    create_outcome = CreateOutcomeMutation.Field()
    update_outcome = UpdateOutcomeMutation.Field()
    delete_outcome = DeleteOutcomeMutation.Field()
