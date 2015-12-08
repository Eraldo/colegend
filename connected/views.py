from braces.views import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import TemplateView, RedirectView

__author__ = 'Eraldo Energy'


class ConnectedView(LoginRequiredMixin, TemplateView):
    template_name = 'connected/connected.html'


class GuidelinesIntroductionView(LoginRequiredMixin, TemplateView):
    template_name = 'connected/guidelines_introduction.html'


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


class GuideIntroductionView(LoginRequiredMixin, TemplateView):
    template_name = 'connected/guide_introduction.html'


class GuideView(LoginRequiredMixin, TemplateView):
    template_name = 'connected/guide.html'


class VirtualRoomView(LoginRequiredMixin, RedirectView):
    permanent = False
    url = 'https://plus.google.com/hangouts/_/colegend42g3psmu3okj5ym27qa'
