from django.core.urlresolvers import reverse_lazy
from gatherings.forms import GatheringForm
from lib.views import ActiveUserRequiredMixin, ManagerRequiredMixin
from django.utils import timezone
from django.utils.timesince import timeuntil
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, ListView
from gatherings.models import Gathering


class GatheringMixin(ManagerRequiredMixin):
    model = Gathering
    form_class = GatheringForm


class GatheringsView(ActiveUserRequiredMixin, TemplateView):
    template_name = "gatherings/gatherings.html"

    def get_context_data(self, **kwargs):
        context = super(GatheringsView, self).get_context_data(**kwargs)
        now = timezone.now()
        # Get next gathering.
        try:
            gathering = Gathering.objects.filter(date__gt=now).last()
        except Gathering.DoesNotExist:
            gathering = None
        if gathering:
            date = gathering.date
            context['date'] = date
            context['counter'] = timeuntil(date, now)
        return context


class GatheringListView(GatheringMixin, ListView):
    pass


class GatheringCreateView(GatheringMixin, CreateView):
    """View for scheduling new gatherings"""
    success_url = reverse_lazy('gatherings:gathering_list')

    def get_initial(self):
        initial = super(GatheringCreateView, self).get_initial()
        initial['date'] = timezone.now()
        return initial


class GatheringEditView(GatheringMixin, UpdateView):
    success_url = reverse_lazy('gatherings:gathering_list')


class GatheringDeleteView(GatheringMixin, DeleteView):
    success_url = reverse_lazy('gatherings:gathering_list')

