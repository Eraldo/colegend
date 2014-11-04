from lib.views import ActiveUserRequiredMixin
from django.utils import timezone
from django.utils.timesince import timeuntil
from django.views.generic import TemplateView
from gatherings.models import Gathering


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
