from gatherings.forms import GatheringForm
from lib.views import ActiveUserRequiredMixin, ManagerRequiredMixin
from django.utils import timezone
from django.utils.timesince import timeuntil
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from gatherings.models import Gathering


class GatheringMixin():
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


class GatheringCreateView(GatheringMixin, CreateView):
    """View for scheduling new gatherings"""


class GatheringEditView(GatheringMixin, UpdateView):
    pass


class GatheringDeleteView(GatheringMixin, DeleteView):
    pass
