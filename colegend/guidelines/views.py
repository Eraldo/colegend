from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect

# Create your views here.
from django.views.generic import TemplateView

# from colegend.games.views import complete_card


class GuidelinesIntroductionView(LoginRequiredMixin, TemplateView):
    template_name = 'guidelines/introduction.html'

    def post(self, request, *args, **kwargs):
        if 'success' in request.POST:
            user = request.user
            user.add_checkpoint('guidelines introduction')
            return redirect('guidelines:index')
        return self.get(request, *args, **kwargs)


class GuidelinesView(LoginRequiredMixin, TemplateView):
    template_name = 'guidelines/index.html'

    def get(self, request, *args, **kwargs):
        user = request.user
        if not user.has_checkpoint('guidelines introduction'):
            return redirect('guidelines:introduction')
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if 'accept' in request.POST:
            user = request.user
            if not user.has_checkpoint('guidelines'):
                pass
                # complete_card(request, 'guidelines')
            return redirect('guidelines:index')
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['guidelines_checkpoint'] = user.has_checkpoint('guidelines')
        return context
