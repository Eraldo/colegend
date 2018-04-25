from enum import Enum

import graphene
from django.utils import timezone

from colegend.core.intuitive_duration.modelfields import IntuitiveDurationField
from colegend.core.intuitive_duration.utils import intuitive_duration_string, parse_intuitive_duration
from colegend.core.utils.icons import Icon
from colegend.experience.models import add_experience

from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphql_relay import from_global_id
from graphene_django.converter import convert_django_field

from colegend.scopes.models import Scope
from colegend.scopes.schema import ScopeType
from .models import Scan, Habit, HabitTrackEvent, HabitReminder, Routine, RoutineHabit


IconType = graphene.Enum.from_enum(Icon)


@convert_django_field.register(IntuitiveDurationField)
def convert_phone_number_to_string(field, registry=None):
    # https://github.com/graphql-python/graphene-django/issues/348
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
            if not user.focuses.filter(scope=Scope.DAY.value, start=today).exists():
                return SuggestedAction.SETTING_FOCUS.value
            if not user.journal_entries.filter(scope=Scope.DAY.value, start=today).exists():
                return SuggestedAction.WRITING_JOURNAL.value
        return None


class HabitNode(DjangoObjectType):
    # https://github.com/graphql-python/graphene-django/issues/348
    duration = graphene.String()
    stats = graphene.List(graphene.Int)

    class Meta:
        model = Habit
        interfaces = [graphene.Node]
        filter_fields = {
            'scope': ['exact'],
        }

    def resolve_duration(self, info, raw=False):
        duration = self.duration
        if raw:
            return duration
        return intuitive_duration_string(duration) if duration is not None else ''

    def resolve_icon(self, info):
        return self.icon or '🔄'

    def resolve_stats(self, info):
        return self.get_stats()


class HabitTrackEventNode(DjangoObjectType):
    class Meta:
        model = HabitTrackEvent
        interfaces = [graphene.Node]


class DeleteHabitTrackMutation(graphene.relay.ClientIDMutation):
    success = graphene.Boolean()

    class Input:
        id = graphene.ID()

    @classmethod
    def mutate_and_get_payload(cls, root, info, id):
        _type, id = from_global_id(id)
        track = HabitTrackEvent.objects.get(id=id)
        track.delete()
        return DeleteHabitTrackMutation(success=True)


class HabitReminderNode(DjangoObjectType):
    class Meta:
        model = HabitReminder
        interfaces = [graphene.Node]


class CreateHabitMutation(graphene.relay.ClientIDMutation):
    success = graphene.Boolean()
    habit = graphene.Field(HabitNode)

    class Input:
        name = graphene.String()
        scope = ScopeType()
        icon = graphene.String()
        duration = graphene.String()
        content = graphene.String()

    @classmethod
    def mutate_and_get_payload(cls, root, info, *args, **kwargs):
        user = info.context.user
        habit = user.habits.create(*args, **kwargs)
        return CreateHabitMutation(success=True, habit=habit)


class UpdateHabitMutation(graphene.relay.ClientIDMutation):
    success = graphene.Boolean()
    habit = graphene.Field(HabitNode)

    class Input:
        id = graphene.ID()
        name = graphene.String()
        scope = ScopeType()
        icon = graphene.String()
        is_active = graphene.Boolean()
        duration = graphene.String()
        content = graphene.String()
        order = graphene.Int()

    @classmethod
    def mutate_and_get_payload(cls, root, info, id, name=None, scope=None, icon=None, is_active=None, duration=None, content=None, order=None):
        user = info.context.user
        _type, id = from_global_id(id)
        habit = user.habits.get(id=id)
        if name is not None:
            habit.name = name
        if scope is not None:
            habit.scope = scope
        if icon is not None:
            habit.icon = icon
        if is_active is not None:
            habit.is_active= is_active
        if duration is not None:
            habit.duration = parse_intuitive_duration(duration)
        if content is not None:
            habit.content = content
        if order is not None:
            habit.to(order)
        habit.save()
        return UpdateHabitMutation(success=True, habit=habit)


class DeleteHabitMutation(graphene.relay.ClientIDMutation):
    success = graphene.Boolean()

    class Input:
        id = graphene.ID()

    @classmethod
    def mutate_and_get_payload(cls, root, info, id):
        user = info.context.user
        _type, id = from_global_id(id)
        habit = user.habits.get(id=id)
        if not habit.is_controlled:
            habit.delete()
        else:
            raise Exception(f'Habit {habit} can only be deleted by the system.')
        return DeleteHabitMutation(success=True)


class TrackHabitMutation(graphene.relay.ClientIDMutation):
    track = graphene.Field(HabitTrackEventNode)

    class Input:
        id = graphene.ID()

    @classmethod
    def mutate_and_get_payload(cls, root, info, id):
        user = info.context.user
        _type, id = from_global_id(id)
        habit = user.habits.get(id=id)
        track = habit.track_events.create()
        return TrackHabitMutation(track=track)


class HabitMutations(graphene.ObjectType):
    create_habit = CreateHabitMutation.Field()
    update_habit = UpdateHabitMutation.Field()
    delete_habit = DeleteHabitMutation.Field()
    track_habit = TrackHabitMutation.Field()
    delete_habit_track = DeleteHabitTrackMutation.Field()


class RoutineNode(DjangoObjectType):
    class Meta:
        model = Routine
        interfaces = [graphene.Node]
        filter_fields = {
            'scope': ['exact'],
        }


class CreateRoutineMutation(graphene.relay.ClientIDMutation):
    success = graphene.Boolean()
    routine = graphene.Field(RoutineNode)

    class Input:
        name = graphene.String()
        scope = ScopeType()
        content = graphene.String()

    @classmethod
    def mutate_and_get_payload(cls, root, info, *args, **kwargs):
        user = info.context.user
        routine = user.routines.create(*args, **kwargs)
        return CreateRoutineMutation(success=True, routine=routine)


class UpdateRoutineMutation(graphene.relay.ClientIDMutation):
    success = graphene.Boolean()
    routine = graphene.Field(RoutineNode)

    class Input:
        id = graphene.ID()
        name = graphene.String()
        scope = ScopeType()
        content = graphene.String()
        order = graphene.Int()
        habits = graphene.List(graphene.String)

    @classmethod
    def mutate_and_get_payload(cls, root, info, id, name=None, scope=None, content=None, order=None, habits=None):
        user = info.context.user
        _type, id = from_global_id(id)
        routine = user.routines.get(id=id)
        if name is not None:
            routine.name = name
        if scope is not None:
            routine.scope = scope
        if content is not None:
            routine.content = content
        if order is not None:
            routine.to(order)
        if habits is not None:
            habit_ids = [from_global_id(id)[1] for id in habits]
            selected_habits = user.habits.filter(id__in=habit_ids)
            current_habits = routine.habits.all()
            # Adding new habits
            for habit in selected_habits:
                if not habit in current_habits:
                    routine.routine_habits.create(habit=habit)
            # Deleting removed habits.
            for habit in current_habits:
                if habit not in selected_habits:
                    routine.routine_habits.get(habit=habit).delete()
        routine.save()
        return UpdateRoutineMutation(success=True, routine=routine)


class DeleteRoutineMutation(graphene.relay.ClientIDMutation):
    success = graphene.Boolean()

    class Input:
        id = graphene.ID()

    @classmethod
    def mutate_and_get_payload(cls, root, info, id):
        user = info.context.user
        _type, id = from_global_id(id)
        routine = user.routines.get(id=id)
        routine.delete()
        return DeleteRoutineMutation(success=True)


class RoutineHabitNode(DjangoObjectType):
    class Meta:
        model = RoutineHabit
        interfaces = [graphene.Node]


class UpdateRoutineHabitMutation(graphene.relay.ClientIDMutation):
    success = graphene.Boolean()
    routine_habit = graphene.Field(RoutineHabitNode)

    class Input:
        id = graphene.ID()
        order = graphene.Int()

    @classmethod
    def mutate_and_get_payload(cls, root, info, id, order=None):
        user = info.context.user
        _type, id = from_global_id(id)
        routine_habit = RoutineHabit.objects.get(id=id)
        if order is not None:
            routine_habit.to(order)
            routine_habit.save()
        return UpdateRoutineHabitMutation(success=True, routine_habit=routine_habit)


class RoutineMutations(graphene.ObjectType):
    create_routine = CreateRoutineMutation.Field()
    update_routine = UpdateRoutineMutation.Field()
    delete_routine = DeleteRoutineMutation.Field()
    update_routine_habit = UpdateRoutineHabitMutation.Field()


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
    def mutate_and_get_payload(cls, root, info, id, area_1=None, area_2=None, area_3=None, area_4=None, area_5=None,
                               area_6=None, area_7=None):
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
    HabitMutations,
    RoutineMutations,
    graphene.ObjectType):
    pass
