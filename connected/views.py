from braces.views import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import TemplateView, RedirectView

from games.views import complete_card

__author__ = 'Eraldo Energy'


class ConnectedView(LoginRequiredMixin, TemplateView):
    template_name = 'connected/connected.html'


class GuidelinesIntroductionView(LoginRequiredMixin, TemplateView):
    template_name = 'connected/guidelines_introduction.html'

    def post(self, request, *args, **kwargs):
        if 'success' in request.POST:
            connected = request.user.connected
            connected.guidelines_introduction = True
            connected.save()
            return redirect('connected:guidelines')
        return self.get(request, *args, **kwargs)


class GuidelinesView(LoginRequiredMixin, TemplateView):
    template_name = 'connected/guidelines.html'

    def get(self, request, *args, **kwargs):
        connected = request.user.connected
        if not connected.guidelines_introduction:
            return redirect('connected:guidelines-introduction')
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if 'accept' in request.POST:
            connected = request.user.connected
            if not connected.guidelines:
                connected.guidelines = True
                connected.save()
                complete_card(request, 'guidelines')
            return redirect('connected:guidelines')
        return self.get(request, *args, **kwargs)


class ChatIntroductionView(LoginRequiredMixin, TemplateView):
    template_name = 'connected/chat_introduction.html'

    def post(self, request, *args, **kwargs):
        if 'success' in request.POST:
            connected = request.user.connected
            connected.chat_introduction = True
            connected.save()
            return redirect('connected:chat-invitation')
        return self.get(request, *args, **kwargs)


class ChatInvitationView(LoginRequiredMixin, TemplateView):
    template_name = 'connected/chat_invitation.html'

    def get(self, request, *args, **kwargs):
        connected = request.user.connected
        if not connected.chat_introduction:
            return redirect('connected:chat-introduction')
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if 'success' in request.POST:
            connected = request.user.connected
            if not connected.chat:
                connected.chat = True
                connected.save()
                complete_card(request, 'chat')
            return redirect('connected:index')


class ChatView(LoginRequiredMixin, RedirectView):
    permanent = False
    url = 'https://colegend.slack.com'

    def get(self, request, *args, **kwargs):
        connected = request.user.connected
        if not connected.chat:
            return redirect('connected:chat-invitation')
        return super().get(request, *args, **kwargs)


class VirtualRoomView(LoginRequiredMixin, RedirectView):
    permanent = False
    url = 'https://plus.google.com/hangouts/_/colegend42g3psmu3okj5ym27qa'
