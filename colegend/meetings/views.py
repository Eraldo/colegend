from lib.views import ActiveUserRequiredMixin
from django.utils import timezone
from django.utils.timesince import timeuntil
from django.views.generic import TemplateView
from meetings.models import Meeting


class MeetingsView(ActiveUserRequiredMixin, TemplateView):
    template_name = "meetings/meetings.html"

    def get_context_data(self, **kwargs):
        context = super(MeetingsView, self).get_context_data(**kwargs)
        now = timezone.now()
        meeting = Meeting.objects.first()
        if meeting and meeting.date > now:
            date = meeting.date
            context['date'] = date
            context['counter'] = timeuntil(date, now)
        return context
