from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect

# Create your views here.
from django.views.generic import RedirectView, TemplateView

from colegend.games.views import complete_card


class ChatIntroductionView(LoginRequiredMixin, TemplateView):
    template_name = 'chat/introduction.html'

    def post(self, request, *args, **kwargs):
        if 'success' in request.POST:
            user = request.user
            user.add_checkpoint('chat introduction')
            return redirect('chat:invitation')
        return self.get(request, *args, **kwargs)


class ChatInvitationView(LoginRequiredMixin, TemplateView):
    template_name = 'chat/invitation.html'

    def get(self, request, *args, **kwargs):
        user = request.user
        if not user.has_checkpoint('chat introduction'):
            return redirect('chat:introduction')
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if 'success' in request.POST:
            user = request.user
            if not user.has_checkpoint('chat'):
                complete_card(request, 'chat')
            return redirect('chat:index')


class ChatView(LoginRequiredMixin, RedirectView):
    permanent = False
    url = 'https://colegend.slack.com'

    def get(self, request, *args, **kwargs):
        user = request.user
        if not user.has_checkpoint('chat'):
            return redirect('chat:invitation')
        return super().get(request, *args, **kwargs)


class VirtualRoomView(LoginRequiredMixin, RedirectView):
    permanent = False
    url = 'https://plus.google.com/hangouts/_/colegend42g3psmu3okj5ym27qa'
