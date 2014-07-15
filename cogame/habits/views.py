from braces.views import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from habits.models import Habit

__author__ = 'eraldo'


class HabitMixin(LoginRequiredMixin):
    model = Habit
    fields = ['routine', 'name', 'tags']


class HabitListView(HabitMixin, ListView):
    pass


class HabitNewView(HabitMixin, CreateView):
    success_url = reverse_lazy('habits:habit_list')


class HabitShowView(HabitMixin, DetailView):
    template_name = "habits/habit_show.html"


class HabitEditView(HabitMixin, UpdateView):
    success_url = reverse_lazy('habits:habit_list')


class HabitDeleteView(HabitMixin, DeleteView):
    success_url = reverse_lazy('habits:habit_list')