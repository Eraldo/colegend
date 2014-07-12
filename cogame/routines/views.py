from django.views.generic import DetailView, View
from routines.models import Routine

__author__ = 'eraldo'


class RoutineMixin:
    model = Routine
    fields = ['name', 'description', 'tags']
    template_name = "routines/routine.html"

    def get_object(self, queryset=None):
        return Routine.objects.get(name=self.routine_name)


class RoutineCheckView(View):
    pass


class RoutineDailyView(RoutineMixin, DetailView):
    routine_name = "daily routine"


class RoutineWeeklyView(RoutineMixin, DetailView):
    routine_name = "weekly routine"


class RoutineMonthlyView(RoutineMixin, DetailView):
    routine_name = "monthly routine"


class RoutineYearlyView(RoutineMixin, DetailView):
    routine_name = "yearly routine"
