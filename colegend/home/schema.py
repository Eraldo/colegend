from enum import Enum

import graphene
from django.utils import timezone

from colegend.core.intuitive_duration.modelfields import IntuitiveDurationField
from colegend.core.intuitive_duration.utils import intuitive_duration_string, parse_intuitive_duration
from colegend.core.utils.icons import Icon
from colegend.experience.models import add_experience

from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphql_relay import from_global_id, to_global_id
from graphene_django.converter import convert_django_field

from colegend.scopes.models import Scope
from colegend.scopes.schema import ScopeType
from .models import Scan, Habit, HabitTrackEvent, HabitReminder, Routine, RoutineHabit, dashboard_habit

IconType = graphene.Enum.from_enum(Icon)


@convert_django_field.register(IntuitiveDurationField)
def convert_phone_number_to_string(field, registry=None):
    # https://github.com/graphql-python/graphene-django/issues/348
    return graphene.String(description=field.help_text, required=not field.null)


class Actions(Enum):
    SETTING_FOCUS = 'setting focus'
    WRITING_JOURNAL = 'writing journal'
    TRACKING_HABIT = 'tracking habit'


ActionTypes = graphene.Enum.from_enum(Actions)


class ActionType(graphene.ObjectType):
    type = graphene.Field(ActionTypes)
    payload = graphene.JSONString()


class SuggestedActionQuery(graphene.ObjectType):
    suggested_action = graphene.Field(ActionType)

    def resolve_suggested_action(self, info):
        user = info.context.user
        today = timezone.localtime(timezone.now()).date()
        if user.is_authenticated:
            if not user.focuses.filter(scope=Scope.DAY.value, start=today).exists():
                return ActionType(type=Actions.SETTING_FOCUS.value)
            if not user.journal_entries.filter(scope=Scope.DAY.value, start=today).exists():
                return ActionType(type=Actions.WRITING_JOURNAL.value)

            # Suggesting next untracked habit
            next_habit = user.habits.active().untracked().first()
            if next_habit:
                id = to_global_id(HabitNode._meta.name, next_habit.id)
                return ActionType(type=Actions.TRACKING_HABIT.value, payload={'id': id, 'name': next_habit.name})

            # TODO: Processing Dashboard streak (v1)
        return None


class DashboardStreakQuery(graphene.ObjectType):
    dashboard_streak = graphene.Int()

    def resolve_dashboard_streak(self, info):
        user = info.context.user

        if user.is_authenticated:
            try:
                habit = user.habits.get(name='Dashboard', is_controlled=True)
            except Habit.DoesNotExist:
                habit = user.habits.create(**dashboard_habit)

            # Tracking only once per day.
            today = timezone.localtime(timezone.now()).date()
            track, created = habit.track_events.get_or_create(created__date=today)
            if created:
                if habit.track_events.filter(created__date=today - timezone.timedelta(days=1)).exists():
                    habit.increase_streak()
                    habit.save()
                else:
                    habit.reset_streak(to=1)
            return habit.streak


# class DashboardCheckMutation(graphene.relay.ClientIDMutation):
#     streak = graphene.Int()
#
#     class Input:
#         pass
#
#     @classmethod
#     def mutate_and_get_payload(cls, root, info):
#         user = info.context.user
#
#         try:
#             habit = user.habits.get(name='Dashboard', is_controlled=True)
#         except Habit.DoesNotExist:
#             habit = user.habits.create(**dashboard_habit)
#
#         # Tracking only once per day.
#         today = timezone.localtime(timezone.now()).date()
#         track, created = habit.track_events.get_or_create(created__date=today)
#         if created:
#             if habit.track_events.filter(created__date=today-timezone.timedelta(days=1)).exists():
#                 habit.increase_streak()
#                 habit.save(update_fields=['streak'])
#             else:
#                 habit.reset_streak()
#         return DashboardCheckMutation(streak=habit.streak)


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
    def mutate_and_get_payload(cls, root, info, id, name=None, scope=None, icon=None, is_active=None, duration=None,
                               content=None, order=None):
        user = info.context.user
        _type, id = from_global_id(id)
        habit = user.habits.get(id=id)

        if not habit.is_controlled:
            if name is not None:
                habit.name = name
            if scope is not None:
                habit.scope = scope
            if icon is not None:
                habit.icon = icon
            if duration is not None:
                habit.duration = parse_intuitive_duration(duration)
            if content is not None:
                habit.content = content
        if is_active is not None:
            habit.is_active = is_active
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

        today = timezone.localtime(timezone.now()).date()

        # TODO: Handle system controlled habits.

        track, created = habit.track_events.get_or_create(created__date=today)
        if created:
            if habit.scope == Scope.DAY.value:
                if habit.track_events.filter(created__date=today - timezone.timedelta(days=1)).exists():
                    habit.increase_streak()
                    habit.save()
                else:
                    habit.reset_streak(to=1)
            # TODO: Implement streak updates / success criteria for other scopes.

        return TrackHabitMutation(track=track)


class HabitMutations(graphene.ObjectType):
    create_habit = CreateHabitMutation.Field()
    update_habit = UpdateHabitMutation.Field()
    delete_habit = DeleteHabitMutation.Field()
    track_habit = TrackHabitMutation.Field()
    delete_habit_track = DeleteHabitTrackMutation.Field()
    # check_dashboard = DashboardCheckMutation.Field()


class RoutineNode(DjangoObjectType):
    duration = graphene.String()

    class Meta:
        model = Routine
        interfaces = [graphene.Node]
        filter_fields = {
            'scope': ['exact'],
        }

    def resolve_duration(self, info):
        return self.duration


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
        routine_habit = RoutineHabit.objects.get(id
                                                 =id)
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


class CreateScanMutation(graphene.relay.ClientIDMutation):
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
        return CreateScanMutation(success=True, scan=scan)


class UpdateScanMutation(graphene.relay.ClientIDMutation):
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
        return UpdateScanMutation(success=True, scan=scan)


class DeleteScanMutation(graphene.relay.ClientIDMutation):
    success = graphene.Boolean()

    class Input:
        id = graphene.ID()

    @classmethod
    def mutate_and_get_payload(cls, root, info, id):
        user = info.context.user
        _type, id = from_global_id(id)
        scan = user.scans.get(id=id)
        scan.delete()
        return DeleteScanMutation(success=True)


class ScanMutation(graphene.ObjectType):
    create_scan = CreateScanMutation.Field()
    update_scan = UpdateScanMutation.Field()
    delete_scan = DeleteScanMutation.Field()


class HomeQuery(
    SuggestedActionQuery,
    DashboardStreakQuery,
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
