import datetime
from braces.views import LoginRequiredMixin
from django.utils.timesince import timeuntil
from django.views.generic import TemplateView


class MeetingsView(LoginRequiredMixin, TemplateView):
    template_name = "meetings/meetings.html"

    def get_counter(self, date):
        now = datetime.datetime.now()
        while date.weekday() != 6:
            date += datetime.timedelta(1)
        return timeuntil(date, now)

    def get_context_data(self, **kwargs):
        context = super(MeetingsView, self).get_context_data(**kwargs)
        now = datetime.datetime.now()
        date = datetime.datetime(now.year, now.month, now.day, 20, 4)
        context['date'] = date
        context['counter'] = self.get_counter(date)
        return context
