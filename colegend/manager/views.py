from django.utils import timezone
from django.views.generic import TemplateView
from lib.views import ActiveUserRequiredMixin


class AgendaView(ActiveUserRequiredMixin, TemplateView):
    template_name = "manager/agenda.html"
    icon = "agenda"
    tutorial = "Agenda"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context["scheduled_tasks"] = user.tasks.open().filter(date__lte=timezone.now()).order_by('date')
        context["next_projects"] = user.projects.next()
        context["next_tasks"] = user.tasks.next().filter(project__isnull=True)
        context["top_deadlined_projects"] = user.projects.open().filter(deadline__isnull=False).order_by('deadline')[:2]
        context["top_deadlined_tasks"] = user.tasks.open().filter(deadline__isnull=False).order_by('deadline')[:4]
        return context
