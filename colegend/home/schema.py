from enum import Enum

import graphene
from django.utils import timezone

from colegend.core.intuitive_duration.modelfields import IntuitiveDurationField
from colegend.experience.models import add_experience
from colegend.scopes.models import DAY

from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphql_relay import from_global_id
from graphene_django.converter import convert_django_field

from .models import Scan, Habit, HabitTrackEvent, HabitReminder, Routine, RoutineHabit


@convert_django_field.register(IntuitiveDurationField)
def convert_phone_number_to_string(field, registry=None):
    return graphene.String(description=field.help_text, required=not field.null)


class SuggestedAction(Enum):
    SETTING_FOCUS = 'setting focus'
    WRITING_JOURNAL = 'writing journal'


SuggestedActionType = graphene.Enum.from_enum(SuggestedAction)


class SuggestedActionQuery(graphene.ObjectType):
    suggested_action = graphene.Field(SuggestedActionType)

    def resolve_suggested_action(self, info):
        user = info.context.user
        today = timezone.localtime(timezone.now()).date()
        if user.is_authenticated:
            if not user.focuses.filter(scope=DAY, start=today).exists():
                return SuggestedAction.SETTING_FOCUS.value
            if not user.journal_entries.filter(scope=DAY, start=today).exists():
                return SuggestedAction.WRITING_JOURNAL.value
        return None


class HabitNode(DjangoObjectType):
    class Meta:
        model = Habit
        interfaces = [graphene.Node]


class HabitTrackEventNode(DjangoObjectType):
    class Meta:
        model = HabitTrackEvent
        interfaces = [graphene.Node]


class HabitReminderNode(DjangoObjectType):
    class Meta:
        model = HabitReminder
        interfaces = [graphene.Node]


class RoutineNode(DjangoObjectType):
    class Meta:
        model = Routine
        interfaces = [graphene.Node]


class RoutineHabitNode(DjangoObjectType):
    class Meta:
        model = RoutineHabit
        interfaces = [graphene.Node]


class ScanNode(DjangoObjectType):
    class Meta:
        model = Scan
        filter_fields = {
            'date': ['exact', 'lt', 'gt', 'lte', 'gte'],
            'area_1': ['exact', 'lt', 'gt', 'lte', 'gte'],
            'area_2': ['exact', 'lt', 'gt', 'lte', 'gte'],
            'area_3': ['exact', 'lt', 'gt', 'lte', 'gte'],
            'area_4': ['exact', 'lt', 'gt', 'lte', 'gte'],
            'area_5': ['exact', 'lt', 'gt', 'lte', 'gte'],
            'area_6': ['exact', 'lt', 'gt', 'lte', 'gte'],
            'area_7': ['exact', 'lt', 'gt', 'lte', 'gte'],
            'owner': ['exact'],
        }
        interfaces = [graphene.Node]


class HabitsQuery(graphene.ObjectType):
    habit = graphene.Node.Field(HabitNode)
    routine = graphene.Node.Field(RoutineNode)


class ScanQuery(graphene.ObjectType):
    scan = graphene.Node.Field(ScanNode)
    scans = DjangoFilterConnectionField(ScanNode)


class CreateScan(graphene.relay.ClientIDMutation):
    success = graphene.Boolean()
    scan = graphene.Field(ScanNode)

    class Input:
        date = graphene.types.datetime.Date()
        area_1 = graphene.Int()
        area_2 = graphene.Int()
        area_3 = graphene.Int()
        area_4 = graphene.Int()
        area_5 = graphene.Int()
        area_6 = graphene.Int()
        area_7 = graphene.Int()

    @classmethod
    def mutate_and_get_payload(cls, root, info, *args, **kwargs):
        user = info.context.user
        scan = user.scans.create(*args, **kwargs)
        add_experience(user, 'home')
        return CreateScan(success=True, scan=scan)


class UpdateScan(graphene.relay.ClientIDMutation):
    success = graphene.Boolean()
    scan = graphene.Field(ScanNode)

    class Input:
        id = graphene.ID()
        area_1 = graphene.Int()
        area_2 = graphene.Int()
        area_3 = graphene.Int()
        area_4 = graphene.Int()
        area_5 = graphene.Int()
        area_6 = graphene.Int()
        area_7 = graphene.Int()

    @classmethod
    def mutate_and_get_payload(cls, root, info, id, area_1=None, area_2=None, area_3=None, area_4=None, area_5=None, area_6=None, area_7=None):
        user = info.context.user
        _type, id = from_global_id(id)
        scan = user.scans.get(id=id)
        if area_1 is not None:
            scan.area_1 = area_1
        if area_2 is not None:
            scan.area_2 = area_2
        if area_3 is not None:
            scan.area_3 = area_3
        if area_4 is not None:
            scan.area_4 = area_4
        if area_5 is not None:
            scan.area_5 = area_5
        if area_6 is not None:
            scan.area_6 = area_6
        if area_7 is not None:
            scan.area_7 = area_7
        scan.save()
        return UpdateScan(success=True, scan=scan)


class DeleteScan(graphene.relay.ClientIDMutation):
    success = graphene.Boolean()

    class Input:
        id = graphene.ID()

    @classmethod
    def mutate_and_get_payload(cls, root, info, id):
        user = info.context.user
        _type, id = from_global_id(id)
        scan = user.scans.get(id=id)
        scan.delete()
        return DeleteScan(success=True)


class ScanMutation(graphene.ObjectType):
    create_scan = CreateScan.Field()
    update_scan = UpdateScan.Field()
    delete_scan = DeleteScan.Field()


class HomeQuery(
    SuggestedActionQuery,
    ScanQuery,
    HabitsQuery,
    graphene.ObjectType):
    pass


class HomeMutation(
    ScanMutation,
    graphene.ObjectType):
    pass
