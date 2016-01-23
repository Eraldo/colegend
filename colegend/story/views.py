import random
from os import path

from braces.views import LoginRequiredMixin
from django.conf import settings
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.utils import timezone
from django.views.generic import TemplateView

from colegend.games.views import complete_card
from .models import WelcomeTreeLeaf


class StoryView(LoginRequiredMixin, TemplateView):
    template_name = "story/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        prologue_buttons = [
            {
                'name': 'Prologue',
                'url': reverse('story:prologue'),
                'condition': True,
            },
            {
                'name': 'Welcome Tree',
                'url': reverse('story:welcome-tree'),
                'condition': user.has_checkpoint('prologue'),
            },
        ]
        context['prologue_buttons'] = prologue_buttons
        chapter1_buttons = [
            {
                'name': 'Entering Leyenda',
                'url': reverse('story:leyenda'),
                'condition': user.has_checkpoint('storytime card'),
            },
            {
                'name': 'Pioneer Journal',
                'url': reverse('story:poineer-journal'),
                'condition': user.has_checkpoint('leyenda'),
            },
            {
                'name': 'The Journal',
                'url': reverse('story:your-journal'),
                'condition': user.has_checkpoint('pioneer journal'),
            },
        ]
        context['chapter1_buttons'] = chapter1_buttons
        return context


class Chapter1View(LoginRequiredMixin, TemplateView):
    template_name = "story/chapter1.html"


class PrologueView(LoginRequiredMixin, TemplateView):
    template_name = "story/prologue.html"

    def get_context_data(self, **kwargs):
        user = self.request.user
        context = super().get_context_data(**kwargs)

        country = self.get_prologue_country()
        context['country'] = country

        weekday = user.date_joined.strftime('%A')
        context['weekday'] = weekday

        time_of_day = self.get_time_of_day(time=user.date_joined)
        context['time_of_day'] = time_of_day

        typed_username = self.get_typed_username()
        context['typed_username'] = typed_username

        context['prologue'] = user.has_checkpoint('prologue')
        return context

    def get_prologue_country(self):
        user = self.request.user
        country = user.continuous.prologue_country
        if not country:
            country = self.get_client_country()
            if country:
                user.continuous.prologue_country = country
                user.continuous.save()
        return country

    @staticmethod
    def get_client_ip(request):
        """
        Reads the ip from the request object and returns it.
        :return: client ip address string
            Example: '89.204.139.76'

        """
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def get_client_country(self):
        """
        Gets the client ip address and returns the corresponding country string.
        :return: Country string
            Example:
            Assumption: ip = '89.204.139.76'
            => 'Germany'
        """
        import pygeoip
        gi = pygeoip.GeoIP(path.join(str(settings.APPS_DIR), 'story/static/story/GeoIP.dat'))
        request = self.request
        ip = self.get_client_ip(request)
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
        if 'welcome-tree' in request.POST:
            user = request.user
            user.checkpoints.create(name='prologue')
            continuous = request.user.continuous
            continuous.chapter = 1
            continuous.save()
            return redirect('story:welcome-tree')


class WelcomeTreeView(LoginRequiredMixin, TemplateView):
    template_name = "story/welcome-tree.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['prologue'] = self.request.user.has_checkpoint('prologue')
        return context


class WelcomeTreeLeafWidgetView(LoginRequiredMixin, TemplateView):
    template_name = 'story/widgets/leaf.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        legend_leaves = WelcomeTreeLeaf.objects.all()
        messages = greetings
        messages += [leaf.content for leaf in legend_leaves]
        context['text'] = random.choice(messages)
        return context


greetings = [
    'Thank you for having the courage to take your story into your own hands.',
    'This world needs people like you, who are willing to go and look for the roots instead of just complaining about the sickened leaves.',
    'I welcome you into the circle of Legends.',
    'I am grateful for everything that has happened so far, as every step has led me to this very moment where you decided to join this community.',
    'To be alive and aware are two of the most wonderful gifts I have ever received.',
    'What can I possibly tell you to make you feel welcome in this space that is as much yours as it is mine? How do we shift the paradigm from either or, to and? I hope you will help us find out…',
    'I was not sent to this world by an unknown force, nor was I born for a greater reason, I have and always will be part of this ecosystem we call earth, galaxy, universe. For this time of a human specimen I decide to work hard to remind ourselves that we were not, are not and never will be, disconnected.',
]


class LeyendaView(LoginRequiredMixin, TemplateView):
    template_name = 'story/leyenda.html'

    def post(self, request, *args, **kwargs):
        post = request.POST
        if 'success' in post:
            user = request.user
            if not user.has_checkpoint(name='leyenda'):
                user.add_checkpoint(name='leyenda')
            return redirect('story:poineer-journal')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['leyenda'] = self.request.user.has_checkpoint('leyenda')
        return context


class PioneerJournalView(LoginRequiredMixin, TemplateView):
    template_name = 'story/poineer_journal.html'

    def post(self, request, *args, **kwargs):
        if 'success' in request.POST:
            user = request.user
            if not user.has_checkpoint('pioneer journal'):
                user.add_checkpoint('pioneer journal')
            return redirect('story:your-journal')


class YourJournalView(LoginRequiredMixin, TemplateView):
    template_name = 'story/your_journal.html'

    def post(self, request, *args, **kwargs):
        if 'success' in request.POST:
            user = request.user
            if not user.has_checkpoint('your journal'):
                user.add_checkpoint('your journal')
                user.continuous.chapter = 2
                user.continuous.save()
                complete_card(request, 'storytime')
            return redirect('story:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['your_journal'] = self.request.user.has_checkpoint('your journal')
        return context
