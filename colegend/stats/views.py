from django.views.generic import TemplateView


class StatsView(TemplateView):
    icon = "stats"
    template_name = "stats/home.html"

    def get_context_data(self, *args, **kwargs):
        user = self.request.user
        context = super().get_context_data(*args, **kwargs)
        context["tasks_total"] = user.tasks.count()
        context["tasks_open"] = user.tasks.open().count()
        context["tasks_closed"] = user.tasks.closed().count()
        context["tasks_next"] = user.tasks.next().count()
        context["tasks_todo"] = user.tasks.status("todo").count()
        context["tasks_waiting"] = user.tasks.status("waiting").count()
        context["tasks_someday"] = user.tasks.status("someday").count()
        context["tasks_maybe"] = user.tasks.status("maybe").count()
        context["tasks_done"] = user.tasks.status("done").count()
        context["tasks_canceled"] = user.tasks.status("canceled").count()
        return context
