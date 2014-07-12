from django.core.urlresolvers import reverse_lazy
from django.views.generic import DetailView, View, ListView, CreateView, UpdateView, DeleteView
from routines.models import Routine

__author__ = 'eraldo'


class RoutineMixin:
    model = Routine
    fields = ['name', 'description', 'tags']
    

class RoutineCheckView(View):
    pass


class RoutineListView(RoutineMixin, ListView):
    def get_queryset(self):
        queryset = super(RoutineListView, self).get_queryset()
        return queryset


class RoutineNewView(RoutineMixin, CreateView):
    success_url = reverse_lazy('routines:routine_list')


class RoutineShowView(RoutineMixin, DetailView):
    template_name = "routines/routine_show.html"

    def get_context_data(self, **kwargs):
        context = super(RoutineShowView, self).get_context_data(**kwargs)
        routine = self.get_object()
        habits = routine.habits.all()
        context["habits"] = habits
        return context


class RoutineEditView(RoutineMixin, UpdateView):
    success_url = reverse_lazy('routines:routine_list')


class RoutineDeleteView(RoutineMixin, DeleteView):
    success_url = reverse_lazy('routines:routine_list')
    

## special routines

class SpecialRoutineMixin(RoutineMixin):
    template_name = "routines/routine_show.html"

    def get_object(self, queryset=None):
        return Routine.objects.get(name=self.routine_name)
    

class RoutineDailyView(SpecialRoutineMixin, DetailView):
    routine_name = "daily routine"
    
    def get_object(self, queryset=None):
        return Routine.objects.get(name=self.routine_name)


    def get_context_data(self, **kwargs):
        context = super(RoutineDailyView, self).get_context_data(**kwargs)
        routine = self.get_object()
        habits = routine.habits.all()
        context["habits"] = habits
        return context


class RoutineWeeklyView(SpecialRoutineMixin, DetailView):
    routine_name = "weekly routine"


class RoutineMonthlyView(SpecialRoutineMixin, DetailView):
    routine_name = "monthly routine"


class RoutineYearlyView(SpecialRoutineMixin, DetailView):
    routine_name = "yearly routine"
