from braces.views import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import TemplateView, RedirectView

__author__ = 'Eraldo Energy'


class ConnectedView(LoginRequiredMixin, TemplateView):
    template_name = 'connected/connected.html'


class GuidelinesIntroductionView(LoginRequiredMixin, TemplateView):
    template_name = 'connected/guidelines_introduction.html'

    def post(self, request, *args, **kwargs):
        if 'success' in request.POST:
            user = request.user
            user.connected.guidelines_introduction = True
            user.connected.save()
            return redirect('connected:guidelines')
        return self.get(request, *args, **kwargs)


class GuidelinesView(LoginRequiredMixin, TemplateView):
    template_name = 'connected/guidelines.html'

    def post(self, request, *args, **kwargs):
        if 'accept' in request.POST:
            user = request.user
            if not user.connected.guidelines:
                user.connected.guidelines = True
                user.connected.save()
            return redirect('connected:guidelines')
        return self.get(request, *args, **kwargs)


class ChatIntroductionView(LoginRequiredMixin, TemplateView):
    template_name = 'connected/chat_introduction.html'

    def post(self, request, *args, **kwargs):
        if 'success' in request.POST:
            user = request.user
            user.connected.chat_introduction = True
            user.connected.save()
            return redirect('connected:chat-invitation')
        return self.get(request, *args, **kwargs)


class ChatInvitationView(LoginRequiredMixin, TemplateView):
    template_name = 'connected/chat_invitation.html'

    def post(self, request, *args, **kwargs):
        if 'success' in request.POST:
            user = request.user
            if not user.connected.chat:
                user.connected.chat = True
                user.connected.save()
            return redirect('connected:index')


class ChatView(LoginRequiredMixin, RedirectView):
    permanent = False
    url = 'https://colegend.slack.com'


class VirtualRoomView(LoginRequiredMixin, RedirectView):
    permanent = False
    url = 'https://plus.google.com/hangouts/_/colegend42g3psmu3okj5ym27qa'
