from django.core.urlresolvers import reverse_lazy, reverse
from gatherings.forms import GatheringForm
from lib.utilities import get_location_url
from lib.views import ActiveUserRequiredMixin, ManagerRequiredMixin
from django.utils import timezone
from django.utils.timesince import timeuntil
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, ListView, RedirectView
from gatherings.models import Gathering


class GatheringMixin():
    model = Gathering
    form_class = GatheringForm
    icon = "gathering"
    tutorial = "Gatherings"


class GatheringsView(ActiveUserRequiredMixin, GatheringMixin, TemplateView):
    template_name = "gatherings/gatherings.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        now = timezone.now()
        current = Gathering.objects.current()
        if current:
            context['current'] = True
        # Get next gathering.
        gathering = Gathering.objects.next()
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
            # virtual room
        context['virtual_room_url'] = reverse("gatherings:room")
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


class GatheringRoomView(ActiveUserRequiredMixin, RedirectView):
    permanent = False
    url = "https://plus.google.com/hangouts/_/g3ci4r3boo5tkipdx4kzpilrfya"
