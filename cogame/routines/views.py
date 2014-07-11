from django.views.generic import TemplateView

__author__ = 'eraldo'


class RoutineMixin:
    pass


class RoutineCheckView(RoutineMixin, TemplateView):
    pass


class RoutineDailyView(RoutineMixin, TemplateView):
    template_name = "routines/routine.html"


class RoutineWeeklyView(RoutineMixin, TemplateView):
    template_name = "routines/routine.html"


class RoutineMonthlyView(RoutineMixin, TemplateView):
    template_name = "routines/routine.html"


class RoutineYearlyView(RoutineMixin, TemplateView):
    template_name = "routines/routine.html"
