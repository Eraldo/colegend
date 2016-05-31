from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import redirect
from django.views.generic import TemplateView, RedirectView

from colegend.games.views import complete_card

__author__ = 'Eraldo Energy'


class ConnectedView(LoginRequiredMixin, TemplateView):
    template_name = 'connected/connected.html'


class GuidelinesIntroductionView(LoginRequiredMixin, TemplateView):
    template_name = 'connected/guidelines_introduction.html'

    def post(self, request, *args, **kwargs):
        if 'success' in request.POST:
            user = request.user
            user.add_checkpoint('guidelines introduction')
            return redirect('connected:guidelines')
        return self.get(request, *args, **kwargs)


class GuidelinesView(LoginRequiredMixin, TemplateView):
    template_name = 'connected/guidelines.html'

    def get(self, request, *args, **kwargs):
        user = request.user
        if not user.has_checkpoint('guidelines introduction'):
            return redirect('connected:guidelines-introduction')
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if 'accept' in request.POST:
            user = request.user
            if not user.has_checkpoint('guidelines'):
                complete_card(request, 'guidelines')
            return redirect('connected:guidelines')
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['guidelines_checkpoint'] = user.has_checkpoint('guidelines')
        return context


class ChatIntroductionView(LoginRequiredMixin, TemplateView):
    template_name = 'connected/chat_introduction.html'

    def post(self, request, *args, **kwargs):
        if 'success' in request.POST:
            user = request.user
            user.add_checkpoint('chat introduction')
            return redirect('connected:chat-invitation')
        return self.get(request, *args, **kwargs)


class ChatInvitationView(LoginRequiredMixin, TemplateView):
    template_name = 'connected/chat_invitation.html'

    def get(self, request, *args, **kwargs):
        user = request.user
        if not user.has_checkpoint('chat introduction'):
            return redirect('connected:chat-introduction')
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if 'success' in request.POST:
            user = request.user
            if not user.has_checkpoint('chat'):
                complete_card(request, 'chat')
            return redirect('connected:index')


class ChatView(LoginRequiredMixin, RedirectView):
    permanent = False
    url = 'https://colegend.slack.com'

    def get(self, request, *args, **kwargs):
        user = request.user
        if not user.has_checkpoint('chat'):
            return redirect('connected:chat-invitation')
        return super().get(request, *args, **kwargs)


class VirtualRoomView(LoginRequiredMixin, RedirectView):
    permanent = False
    url = 'https://plus.google.com/hangouts/_/colegend42g3psmu3okj5ym27qa'
