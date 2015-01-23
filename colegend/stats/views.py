from django.utils import timezone
from django.utils.timesince import timesince
from django.views.generic import TemplateView
from challenges.models import Challenge
from features.models import Feature
from gatherings.models import Gathering
from lib.views import ActiveUserRequiredMixin, ManagerRequiredMixin
from news.models import NewsBlock
from notifications.models import Notification
from projects.models import Project
from quotes.models import Quote
from tags.models import Tag
from tasks.models import Task
from trackers.models import TRACKERS
from tutorials.models import Tutorial
from users.models import User
from visions.models import Vision


class StatsView(ActiveUserRequiredMixin, TemplateView):
    icon = "stats"
    template_name = "stats/home.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        user = self.request.user
        # User
        context["user_days"] = timesince(user.date_joined)
        # Journal
        context["journal_entries"] = user.journal.entries.count()
        context["journal_streak"] = user.journal.streak
        context["journal_max_streak"] = user.journal.max_streak
        # Tasks
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
        # Projects
        context["projects_total"] = user.projects.count()
        context["projects_open"] = user.projects.open().count()
        context["projects_closed"] = user.projects.closed().count()
        context["projects_next"] = user.projects.next().count()
        context["projects_todo"] = user.projects.status("todo").count()
        context["projects_waiting"] = user.projects.status("waiting").count()
        context["projects_someday"] = user.projects.status("someday").count()
        context["projects_maybe"] = user.projects.status("maybe").count()
        context["projects_done"] = user.projects.status("done").count()
        context["projects_canceled"] = user.projects.status("canceled").count()
        # Tags
        context["tags_total"] = user.tags.count()
        # quotes
        context["quotes_total"] = user.quote_set.count()
        # Notifications
        context["notifications_total"] = user.notifications.count()
        context["notifications_read"] = user.notifications.read().count()
        context["notifications_unread"] = user.notifications.unread().count()
        return context


class ManagerStatsView(ManagerRequiredMixin, TemplateView):
    icon = "stats"
    template_name = "stats/manager.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        user = self.request.user

        # Mentor
        context["visions_total"] = Vision.objects.count()
        context["gatherings_total"] = Gathering.objects.count()
        context["challenges_total"] = Challenge.objects.count()

        # Manager
        context["tasks_total"] = Task.objects.count()
        context["projects_total"] = Project.objects.count()
        context["tags_total"] = Tag.objects.count()
        tracks = 0
        for tracker in TRACKERS:
            tracks += tracker.objects.count()
        context["tracks_total"] = tracks

        # Motivator
        context["quotes_total"] = Quote.objects.count()

        # Operator
        context["features_total"] = Feature.objects.count()
        context["tutorials_total"] = Tutorial.objects.count()
        context["news_total"] = NewsBlock.objects.count()
        context["notifications_total"] = Notification.objects.count()
        # # Users
        context["users_total"] = User.objects.count()
        context["users_accepted"] = User.objects.accepted().count()
        now = timezone.now()
        context["users_joined_this_month"] = User.objects.filter(date_joined__gte=now.replace(day=1))
        context["users_joined_last_month"] = User.objects.filter(
            date_joined__range=(
                now.replace(day=1) - timezone.timedelta(weeks=4),
                now.replace(day=1)
            )
        )
        context["male_percent"] = User.objects.accepted().filter(contact__gender='M').count() / context[
            "users_accepted"] * 100
        context["female_percent"] = User.objects.accepted().filter(contact__gender='F').count() / context[
            "users_accepted"] * 100
        return context
