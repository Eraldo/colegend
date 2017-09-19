import graphene

from colegend.journals.models import JournalEntry
from colegend.office.models import Focus
from colegend.outcomes.models import Outcome
from colegend.scopes.models import Scope, get_scope_by_name
from colegend.scopes.schema import ScopeType
from colegend.users.models import User


class Metric(graphene.ObjectType):
    users = graphene.Int(scope=ScopeType())

    def resolve_users(self, info, scope=None):
        kwargs = {}
        if scope is not None:
            kwargs['date_joined__gte'] = get_scope_by_name(scope)().start
        return User.objects.filter(**kwargs).count()

    active_users = graphene.Int(scope=ScopeType())

    def resolve_active_users(self, info, scope=Scope.MONTH.value):
        start = get_scope_by_name(scope)().start
        return User.objects.filter(experience__created__gte=start).distinct().count()

    journal_entries = graphene.Int(scope=ScopeType())

    def resolve_journal_entries(self, info, scope=None):
        kwargs = {}
        if scope is not None:
            kwargs['created__gte'] = get_scope_by_name(scope)().start
        return JournalEntry.objects.filter(**kwargs).count()

    outcomes = graphene.Int(scope=ScopeType())

    def resolve_outcomes(self, info, scope=None):
        kwargs = {}
        if scope is not None:
            kwargs['created__gte'] = get_scope_by_name(scope)().start
        return Outcome.objects.filter(**kwargs).count()

    focuses = graphene.Int(scope=ScopeType())

    def resolve_focuses(self, info, scope=None):
        kwargs = {}
        if scope is not None:
            kwargs['created__gte'] = get_scope_by_name(scope)().start
        return Focus.objects.filter(**kwargs).count()

    gender_quote = graphene.String(scope=ScopeType())

    def resolve_gender_quote(self, info, scope=None):
        kwargs = {}
        if scope is not None:
            kwargs['date_joined__gte'] = get_scope_by_name(scope)().start
        males = User.objects.filter(**kwargs).filter(gender=User.MALE).count()
        females = User.objects.filter(**kwargs).filter(gender=User.FEMALE).count()
        neutrals = User.objects.filter(**kwargs).filter(gender=User.NEUTRAL).count()
        total = males + females + neutrals
        if not total:
            return '0% male, 0% female, 0% neutral'
        return '{males:.0f}% male, {females:.0f}% female, {neutrals:.0f}% neutral'.format(
            males=males / total * 100, females=females / total * 100, neutrals=neutrals / total * 100)


class MetricsQuery(graphene.ObjectType):
    metrics = graphene.Field(Metric)

    def resolve_metrics(self, info):
        return Metric()

        # def resolve_metrics(self, info):
        #     data = {}
        #     data['users'] = User.objects.count()
        #     return [Metric(key=key, value=value) for key, value in data.items()]
