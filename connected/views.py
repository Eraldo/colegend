from braces.views import LoginRequiredMixin
from django.views.generic import TemplateView, RedirectView

__author__ = 'Eraldo Energy'


class ConnectedView(LoginRequiredMixin, TemplateView):
    template_name = 'connected/connected.html'


class GuidelinesIntroductionView(LoginRequiredMixin, TemplateView):
    template_name = 'connected/guidelines_introduction.html'


class GuidelinesView(LoginRequiredMixin, TemplateView):
    template_name = 'connected/guidelines.html'


class ChatIntroductionView(LoginRequiredMixin, TemplateView):
    template_name = 'connected/chat_introduction.html'


class ChatInvitationView(LoginRequiredMixin, TemplateView):
    template_name = 'connected/chat_invitation.html'


class ChatView(LoginRequiredMixin, RedirectView):
    permanent = False
    url = 'https://colegend.slack.com'


class VirtualRoomView(LoginRequiredMixin, RedirectView):
    permanent = False
    url = 'https://plus.google.com/hangouts/_/colegend42g3psmu3okj5ym27qa'
