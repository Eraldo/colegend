from django.core.urlresolvers import reverse_lazy
from gatherings.forms import GatheringForm
from lib.utilities import get_location_url
from lib.views import ActiveUserRequiredMixin, ManagerRequiredMixin, get_icon
from django.utils import timezone
from django.utils.timesince import timeuntil
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, ListView
from gatherings.models import Gathering
from tutorials.models import get_tutorial


class GatheringMixin():
    model = Gathering
    form_class = GatheringForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["icon"] = get_icon("comments-o")
        return context


class GatheringsView(ActiveUserRequiredMixin, TemplateView):
    template_name = "gatherings/gatherings.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        now = timezone.now()
        # Get next gathering.
        try:
            gathering = Gathering.objects.filter(
                start__gte=now - timezone.timedelta(hours=1)
            ).last()
        except Gathering.DoesNotExist:
            gathering = None
        if gathering:
            context['start'] = gathering.start
            context['online'] = gathering.online
            if gathering.online:
                location = "Virtual Room"
                url = gathering.location
            else:
                location = gathering.location
                url = get_location_url(gathering.location)
            context['location'] = location
            context['url'] = url
            context['counter'] = timeuntil(gathering.start, now)
            context['host'] = gathering.host
            # scheduled gatherings
            context['future_gatherings'] = Gathering.objects.filter(start__gt=gathering.start)
            # tutorial
            context['tutorial'] = get_tutorial("Gatherings")
        return context


class GatheringListView(ManagerRequiredMixin, GatheringMixin, ListView):
    pass


class GatheringCreateView(ManagerRequiredMixin, GatheringMixin, CreateView):
    """View for scheduling new gatherings"""
    success_url = reverse_lazy('gatherings:gathering_list')

    def get_initial(self):
        initial = super(GatheringCreateView, self).get_initial()
        now = timezone.now()
        try:
            last_gathering = Gathering.objects.first()
            last_start = timezone.localtime(last_gathering.start)
            last_end = timezone.localtime(last_gathering.end)
        except Gathering.DoesNotExist:
            last_start = now
        initial['start'] = timezone.datetime.combine(now.date(), last_start.time())
        # TODO: Test/Fix: What happens when last end was after midnight?
        # idea: Instead of using today's date.. add the day difference to the old end time.
        initial['end'] = timezone.datetime.combine(now.date(), last_end.time())
        return initial

    def form_valid(self, form):
        user = self.request.user
        form.instance.host = user
        return super().form_valid(form)


class GatheringEditView(ManagerRequiredMixin, GatheringMixin, UpdateView):
    success_url = reverse_lazy('gatherings:gathering_list')


class GatheringDeleteView(ManagerRequiredMixin, GatheringMixin, DeleteView):
    template_name = "confirm_delete.html"
    success_url = reverse_lazy('gatherings:gathering_list')

