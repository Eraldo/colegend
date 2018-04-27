import graphene
from django.utils import timezone
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphql_relay import from_global_id

from colegend.api.models import CountableConnectionBase
from colegend.office.types import StatusType
from colegend.outcomes.elo import calculate_elo
from colegend.outcomes.filters import OutcomeFilter, StepFilter
from colegend.scopes.schema import ScopeType

from .models import Outcome, Step


class OutcomeNode(DjangoObjectType):
    class Meta:
        model = Outcome
        interfaces = [graphene.Node]
        connection_class = CountableConnectionBase


class OutcomeQuery(graphene.ObjectType):
    outcome = graphene.Node.Field(OutcomeNode)
    outcomes = DjangoFilterConnectionField(OutcomeNode, filterset_class=OutcomeFilter)
    outcome_match = graphene.List(OutcomeNode)

    def resolve_outcome_match(self, info):
        user = info.context.user
        outcomes = user.outcomes.filter(status=Outcome.CURRENT)
        contestant = outcomes.order_by('comparisons').first()

        if contestant:
            score = contestant.score
            candidates = outcomes.exclude(pk=contestant.pk)

            # Only provisional ones if possible.
            provisioned = candidates.filter(comparisons__gte=10)
            candidates = provisioned or candidates

            # Find an equal or better competitor. Or a worse one if there is none.
            better = candidates.filter(score__gte=score).order_by('score').first()
            worse = candidates.filter(score__lt=score).order_by('-score').first()
            competitor = better or worse

            return [contestant, competitor]


class CreateOutcomeMutation(graphene.relay.ClientIDMutation):
    success = graphene.Boolean()
    outcome = graphene.Field(OutcomeNode)

    class Input:
        name = graphene.String()
        description = graphene.String()
        status = StatusType()
        inbox = graphene.Boolean()
        scope = ScopeType()
        date = graphene.types.datetime.Date()
        deadline = graphene.types.datetime.Date()
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
        date = graphene.types.datetime.Date()
        deadline = graphene.types.datetime.Date()
        estimate = graphene.String()
        tags = graphene.List(graphene.ID)
        deletions = graphene.List(graphene.String)

    @classmethod
    def mutate_and_get_payload(
        cls, root, info, id,
        name=None, description=None, status=None, inbox=None,
        scope=None, date=None, deadline=None, estimate=None, tags=None, deletions=None):
        user = info.context.user
        _type, id = from_global_id(id)
        outcome = user.outcomes.get(id=id)
        if name is not None:
            outcome.name = name
        if description is not None:
            outcome.description = description
        if status is not None:
            # Adding a completion date if newly completed.
            if status == outcome.DONE and not outcome.completed_at:
                outcome.completed_at = timezone.now()
            # Resetting score on status change.
            if status != outcome.status:
                outcome.score = 1000
                outcome.comparisons = 0
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
        if tags is not None:
            tag_ids = [from_global_id(id)[1] for id in tags]
            tags = user.tags.filter(id__in=tag_ids)
            outcome.tags.set(tags)
        if deletions is not None:
            for field in deletions:
                setattr(outcome, field, None)
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


class MatchOutcomesMutation(graphene.relay.ClientIDMutation):
    success = graphene.Boolean()
    contestant = graphene.Field(OutcomeNode)
    competitor = graphene.Field(OutcomeNode)

    class Input:
        contestant = graphene.ID()
        competitor = graphene.ID()
        success = graphene.Boolean()

    @classmethod
    def mutate_and_get_payload(cls, root, info, contestant, competitor, success):
        user = info.context.user
        _type, contestant = from_global_id(contestant)
        _type, competitor = from_global_id(competitor)

        # print(contestant, competitor, success)
        try:
            contestant = user.outcomes.get(id=contestant)
            competitor = user.outcomes.get(id=competitor)
        except Exception as error:
            raise Exception(error)

        # New score for competitor
        if not contestant.is_provisional:
            competitor.score = calculate_elo(competitor.score, contestant.score, not success)
            competitor.save(update_fields=['score', 'comparisons'])

        # New score for contestant
        contestant.score = calculate_elo(contestant.score, competitor.score, success)
        contestant.comparisons = contestant.comparisons + 1
        contestant.save(update_fields=['score', 'comparisons'])

        return MatchOutcomesMutation(success=True, contestant=contestant, competitor=competitor)


class ResetOutcomesScoreMutation(graphene.relay.ClientIDMutation):
    success = graphene.Boolean()

    class Input:
        id = graphene.ID()

    @classmethod
    def mutate_and_get_payload(cls, root, info, id):
        user = info.context.user
        outcomes = user.outcomes
        if id:
            _type, id = from_global_id(id)
            outcomes = outcomes.filter(id=id)
        outcomes.update(score=1000)
        return DeleteOutcomeMutation(success=True)


class OutcomeMutation(graphene.ObjectType):
    create_outcome = CreateOutcomeMutation.Field()
    update_outcome = UpdateOutcomeMutation.Field()
    delete_outcome = DeleteOutcomeMutation.Field()
    match_outcomes = MatchOutcomesMutation.Field()
    reset_outcomes_score = ResetOutcomesScoreMutation.Field()


class StepNode(DjangoObjectType):
    class Meta:
        model = Step
        interfaces = [graphene.Node]


class StepQuery(graphene.ObjectType):
    step = graphene.Node.Field(StepNode)
    steps = DjangoFilterConnectionField(StepNode, filterset_class=StepFilter)


class CreateStepMutation(graphene.relay.ClientIDMutation):
    success = graphene.Boolean()
    step = graphene.Field(StepNode)

    class Input:
        outcome = graphene.ID()
        name = graphene.String()
        order = graphene.Int()

    @classmethod
    def mutate_and_get_payload(cls, root, info, outcome, name, order=None):
        user = info.context.user
        _type, id = from_global_id(outcome)
        outcome = user.outcomes.get(id=id)
        step = outcome.steps.create(name=name)
        return CreateStepMutation(success=True, step=step)


class UpdateStepMutation(graphene.relay.ClientIDMutation):
    success = graphene.Boolean()
    step = graphene.Field(StepNode)

    class Input:
        id = graphene.ID()
        name = graphene.String()
        toggle = graphene.Boolean()
        order = graphene.Int()

    @classmethod
    def mutate_and_get_payload(cls, root, info, id, name=None, toggle=None, order=None):
        user = info.context.user
        _type, id = from_global_id(id)
        # TODO: Checking permission.
        step = Step.objects.get(id=id)
        if name is not None:
            step.name = name
        if toggle is not None:
            step.toggle()
        if order is not None:
            step.to(order)
        step.save()
        return UpdateStepMutation(success=True, step=step)


class DeleteStepMutation(graphene.relay.ClientIDMutation):
    success = graphene.Boolean()

    class Input:
        id = graphene.ID()

    @classmethod
    def mutate_and_get_payload(cls, root, info, id):
        user = info.context.user
        _type, id = from_global_id(id)
        # TODO: Checking permission.
        step = Step.objects.get(id=id)
        step.delete()
        return DeleteStepMutation(success=True)


class StepMutation(graphene.ObjectType):
    create_step = CreateStepMutation.Field()
    update_step = UpdateStepMutation.Field()
    delete_step = DeleteStepMutation.Field()
