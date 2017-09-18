import graphene
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphql_relay import from_global_id

from colegend.outcomes.schema import OutcomeQuery, OutcomeMutation
from colegend.scopes.schema import ScopeType
from .models import Focus


class FocusNode(DjangoObjectType):
    class Meta:
        model = Focus
        filter_fields = {
            'scope': ['exact'],
            'start': ['exact', 'lt', 'gt', 'lte', 'gte'],
            'end': ['exact', 'lt', 'gt', 'lte', 'gte'],
        }
        interfaces = [graphene.Node]


class FocusQuery(graphene.ObjectType):
    focus = graphene.Node.Field(FocusNode)
    focuses = DjangoFilterConnectionField(FocusNode)


class UpdateFocusMutation(graphene.relay.ClientIDMutation):
    success = graphene.Boolean()
    focus = graphene.Field(FocusNode)

    class Input:
        id = graphene.ID()
        scope = ScopeType()
        start = graphene.types.datetime.DateTime()
        outcome1 = graphene.ID()
        outcome2 = graphene.ID()
        outcome3 = graphene.ID()
        outcome4 = graphene.ID()
        reason = graphene.String()

    @classmethod
    def mutate_and_get_payload(
        cls, root, info, id=None,
        scope=None, start=None,
        outcome1=None, outcome2=None, outcome3=None, outcome4=None, reason=None):
        user = info.context.user
        if id is not None and reason is not None:
            _type, id = from_global_id(id)
            focus = user.focuses.get(id=id)
        elif scope is not None and start is not None:
            focus, created = user.focuses.get_or_create(scope=scope, start=start)
        else:
            raise Exception('ID or scope and start needed to get focus.')

        if outcome1 is not None:
            focus.outcome1 = outcome1
        if outcome2 is not None:
            focus.outcome2 = outcome2
        if outcome3 is not None:
            focus.outcome3 = outcome3
        if outcome4 is not None:
            focus.outcome4 = outcome4
        if reason is not None:
            focus.reason = reason
        focus.save()
        return UpdateFocusMutation(success=True, focus=focus)


class FocusMutation(graphene.ObjectType):
    update_focus = UpdateFocusMutation.Field()


class OfficeQuery(
    OutcomeQuery,
    FocusQuery,
    graphene.ObjectType):
    pass


class OfficeMutation(
    OutcomeMutation,
    FocusMutation,
    graphene.ObjectType):
    pass
