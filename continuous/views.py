from annoying.functions import get_object_or_None
from braces.views import LoginRequiredMixin
from django.views.generic import TemplateView

__author__ = 'Eraldo Energy'


class ContinuousView(LoginRequiredMixin, TemplateView):
    template_name = 'continuous/continuous.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        if user.continuous.chapter == 1:
            progress = self.get_chapter_1_progress()
        else:
            progress = '4'
        context['progress'] = progress

        return context

    def get_chapter_1_progress(self):
        user = self.request.user
        completed = 0
        steps = [
            hasattr(user, 'outercall'),
            hasattr(user, 'innercall'),
            user.legend.biography,
            user.connected.guidelines,
            user.connected.chat,
            user.connected.guide,
            # TODO: story chapter 1 steps
        ]
        for step in steps:
            if step:
                completed += 1
        return int(completed / len(steps) * 100)
