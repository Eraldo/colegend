from enum import Enum

import graphene
from django.utils import timezone

from colegend.scopes.models import DAY


class SuggestedAction(Enum):
    SETTING_FOCUS = 'setting focus'
    WRITING_JOURNAL = 'writing journal'


SuggestedActionType = graphene.Enum.from_enum(SuggestedAction)


class SuggestedActionQuery(graphene.ObjectType):
    suggested_action = graphene.Field(SuggestedActionType)

    def resolve_suggested_action(self, info):
        user = info.context.user
        today = timezone.localtime(timezone.now()).date()
        if not user.focuses.filter(scope=DAY, start=today).exists():
            return SuggestedAction.SETTING_FOCUS.value
        if not user.journal_entries.filter(scope=DAY, start=today).exists():
            return SuggestedAction.WRITING_JOURNAL.value


class HomeQuery(
    SuggestedActionQuery,
    graphene.ObjectType):
    pass


class HomeMutation(
    graphene.ObjectType):
    pass
