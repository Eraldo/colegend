from django.contrib import messages
from django.core.urlresolvers import reverse_lazy, reverse
from django.shortcuts import redirect
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
            if gathering.end.date() == gathering.start.date():
                end = timezone.localtime(gathering.end).time()
            else:
                end = gathering.end
            context['end'] = end
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
            context['topic'] = gathering.topic
            context['notes'] = gathering.notes
            # scheduled gatherings
            context['future_gatherings'] = Gathering.objects.filter(start__gt=gathering.start)
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
    url = "https://plus.google.com/hangouts/_/gxonem3dddqdesvz3rv3djdmdya"

    def get(self, request, *args, **kwargs):
        current = Gathering.objects.current(tolerance=timezone.timedelta(minutes=30))
        user = request.user
        if current and user not in current.participants.all():
            current.participants.add(user)
            message = "You have been added as a participant of the current gathering: {}.".format(current)
            messages.add_message(request, messages.INFO, message)
        next_url = request.GET.get("next")
        if next_url:
            redirect(next_url)
        return super().get(request, *args, **kwargs)
