from braces.views import LoginRequiredMixin
from django.shortcuts import redirect
from django.utils import timezone
from django.views.generic import TemplateView


class Chapter1View(LoginRequiredMixin, TemplateView):
    template_name = "legend/chapter1.html"


class PrologueView(LoginRequiredMixin, TemplateView):
    template_name = "legend/prologue.html"

    def get_context_data(self, **kwargs):
        user = self.request.user
        context = super().get_context_data(**kwargs)

        country = self.get_client_country()
        context['country'] = country

        weekday = user.date_joined.strftime('%A')
        context['weekday'] = weekday

        time_of_day = self.get_time_of_day(time=user.date_joined)
        context['time_of_day'] = time_of_day

        typed_username = self.get_typed_username()
        context['typed_username'] = typed_username

        return context

    def get_client_ip(self):
        x_forwarded_for = self.request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = self.request.META.get('REMOTE_ADDR')
        return ip

    def get_client_country(self):
        import pygeoip
        gi = pygeoip.GeoIP('continuous/legend/static/legend/GeoIP.dat')
        ip = self.get_client_ip()
        country = gi.country_name_by_addr(ip)
        return country

    def get_typed_username(self):
        username = self.request.user.username.title()
        typed_username = '^400'.join(username)
        return typed_username

    @staticmethod
    def get_time_of_day(time=timezone.now()):
        # TODO: Check if timezone needs correction (make aware)
        hour = time.hour
        if 4 < hour < 12:  # 5-11 (7h)
            return 'morning'
        elif hour < 18:  # 12-17 (6h)
            return 'afternoon'
        elif hour < 23:  # 18-22 (5h)
            return 'evening'
        else:  # 23-4 (6h)
            return 'night'

    def post(self, request, *args, **kwargs):
        if 'poetree' in request.POST:
            user = request.user
            user.continuous.prologue = True
            user.continuous.save()
            return redirect('continuous:legend:poetree')


class PoetreeView(LoginRequiredMixin, TemplateView):
    template_name = "legend/poetree.html"
