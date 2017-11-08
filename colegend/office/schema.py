import graphene
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphql_relay import from_global_id

from colegend.experience.models import add_experience
from colegend.office.filters import FocusFilter
from colegend.outcomes.schema import OutcomeQuery, OutcomeMutation
from colegend.scopes.schema import ScopeType
from .models import Focus
from .views import notify_partners


class FocusNode(DjangoObjectType):
    class Meta:
        model = Focus
        interfaces = [graphene.Node]


class FocusQuery(graphene.ObjectType):
    focus = graphene.Node.Field(FocusNode)
    focuses = DjangoFilterConnectionField(FocusNode, filterset_class=FocusFilter)


class UpdateFocusMutation(graphene.relay.ClientIDMutation):
    success = graphene.Boolean()
    focus = graphene.Field(FocusNode)

    class Input:
        id = graphene.ID()
        scope = ScopeType()
        start = graphene.types.datetime.DateTime()
        outcome_1 = graphene.ID()
        outcome_2 = graphene.ID()
        outcome_3 = graphene.ID()
        outcome_4 = graphene.ID()
        reason = graphene.String()

    @classmethod
    def mutate_and_get_payload(
        cls, root, info, id=None,
        scope=None, start=None,
        outcome_1=None, outcome_2=None, outcome_3=None, outcome_4=None, reason=None):
        user = info.context.user
        if start:
            # Converting datetime (input parameter type) to date.
            start = start.date()
        if id is not None and reason is not None:
            _type, id = from_global_id(id)
            focus = user.focuses.get(id=id)
        elif scope is not None and start is not None:
            focus, created = user.focuses.get_or_create(scope=scope, start=start)
            if created:
                add_experience(user, 'office')
        else:
            raise Exception('ID or scope and start needed to get focus.')

        old_outcomes = focus.outcomes

        if outcome_1 is not None:
            focus.outcome_1 = user.outcomes.get(id=from_global_id(outcome_1)[1])
        if outcome_2 is not None:
            focus.outcome_2 = user.outcomes.get(id=from_global_id(outcome_2)[1])
        if outcome_3 is not None:
            focus.outcome_3 = user.outcomes.get(id=from_global_id(outcome_3)[1])
        if outcome_4 is not None:
            focus.outcome_4 = user.outcomes.get(id=from_global_id(outcome_4)[1])
        focus.save()
        new_outcomes = focus.outcomes

        # Informing users of update! (using reason if not new).
        notify_partners(focus, reason, old_outcomes, new_outcomes)

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
