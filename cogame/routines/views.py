from django.views.generic import TemplateView

__author__ = 'eraldo'


class RoutineMixin:
    pass


class RoutineCheckView(RoutineMixin, TemplateView):
    template_name = "routines/routine_check.html"


class RoutineDailyView(RoutineMixin, TemplateView):
    template_name = "routines/routine_daily.html"


class RoutineWeeklyView(RoutineMixin, TemplateView):
    template_name = "routines/routine_weekly.html"


class RoutineMonthlyView(RoutineMixin, TemplateView):
    template_name = "routines/routine_monthly.html"


class RoutineYearlyView(RoutineMixin, TemplateView):
    template_name = "routines/routine_yearly.html"
