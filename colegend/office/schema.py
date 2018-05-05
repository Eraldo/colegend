import graphene
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphql_relay import from_global_id

from colegend.experience.models import add_experience
from colegend.office.filters import FocusFilter
from colegend.outcomes.schema import OutcomeQuery, OutcomeMutation, StepQuery, StepMutation
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
        start = graphene.types.datetime.Date()
        outcomes = graphene.List(graphene.ID)
        reason = graphene.String()

    @classmethod
    def mutate_and_get_payload(
        cls, root, info, id=None, scope=None, start=None, **kwargs):
        user = info.context.user

        if not kwargs.get('outcomes'):
            raise Exception('No outcomes provided for focus.')

        if id is not None and 'reason' in kwargs:
            _type, id = from_global_id(id)
            focus = user.focuses.get(id=id)
        elif scope is not None and start is not None:
            focus, created = user.focuses.get_or_create(scope=scope, start=start)
            if created:
                add_experience(user, 'office')
        else:
            raise Exception('ID or scope and start needed to get focus.')

        if 'outcomes' in kwargs:
            # TODO: Replace workaround (for removing outcomes).
            focus.outcome_1 = None
            focus.outcome_2 = None
            focus.outcome_3 = None
            focus.outcome_4 = None

            outcome_ids = [from_global_id(id)[1] for id in kwargs.get('outcomes', [])]
            new_outcomes = user.outcomes.filter(id__in=outcome_ids)
            for index, outcome in enumerate(new_outcomes):
                setattr(focus, f'outcome_{index+1}', outcome)
        focus.save()

        return UpdateFocusMutation(success=True, focus=focus)


class FocusMutation(graphene.ObjectType):
    update_focus = UpdateFocusMutation.Field()


class OfficeQuery(
    OutcomeQuery,
    StepQuery,
    FocusQuery,
    graphene.ObjectType):
    pass


class OfficeMutation(
    OutcomeMutation,
    StepMutation,
    FocusMutation,
    graphene.ObjectType):
    pass
