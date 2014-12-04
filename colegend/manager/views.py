from django.views.generic import TemplateView
from lib.views import ActiveUserRequiredMixin, get_icon
from tutorials.models import get_tutorial


class AgendaView(ActiveUserRequiredMixin, TemplateView):
    template_name = "manager/agenda.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["icon"] = get_icon("crosshairs")
        user = self.request.user
        context["top_projects"] = user.projects.open()[:3]
        context["top_deadline_tasks"] = user.tasks.open().filter(deadline__isnull=False).order_by('deadline')[:4]
        context["single_tasks"] = user.tasks.open().filter(project__isnull=True)[:4]
        context['tutorial'] = get_tutorial("Agenda")
        return context
