from braces.views import LoginRequiredMixin
from django.views.generic import DetailView, UpdateView, ListView

from legends.forms import LegendForm
from .models import Legend


class LegendDetailView(LoginRequiredMixin, DetailView):
    template_name = 'legends/detail.html'
    model = Legend

    def get_object(self, queryset=None):
        owner = self.kwargs.get('owner')
        if owner:
            return Legend.objects.get(owner__username=owner)
        else:
            return self.request.user.legend


class LegendUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'legends/update.html'
    model = Legend
    form_class = LegendForm

    def get_object(self, queryset=None):
        owner = self.kwargs.get('owner')
        if owner:
            return Legend.objects.get(owner__username=owner)
        else:
            return self.request.user.legend


class LegendListView(LoginRequiredMixin, ListView):
    template_name = 'legends/list.html'
    model = Legend
    context_object_name = 'legends'
