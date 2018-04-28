from django.core.management.base import BaseCommand
from django.template.loader import render_to_string
from django.utils import timezone

from colegend.journals.scopes import Day
from colegend.office.models import Focus
from colegend.scopes.models import Scope
from colegend.users.models import User


class Command(BaseCommand):
    help = 'Generates user focus reports'

    def handle(self, *args, **options):
        """
        Check if the user's focus status and create a report for his partner(s).
        Is supposed to run after midday.

        Only Taking premium users into account.

        General solution idea:
        1. Filtering users: only primary users who have a duo.
        2. Generating a pre-day status report:
            Per outcome:
                Green: User completed min 1 step.
                Yellow: Next step is defined.
                Red: No next step defined.
        3. Generate a current day status report:
            Per outcome:
                Outcome Name
                    Next step

        Next version:
            Html report.
        """

        date = timezone.localtime(timezone.now()).date()
        self.stdout.write(f'# Generating day focus reports for {date}')
        users = User.objects.filter(is_active=True, is_premium=True, duo__isnull=False)
        scope = Day(date=date)
        for user in users:
            context = {'user': user, 'date': date}

            recipients = user.duo.members.values_list('email', flat=True)
            if not recipients:
                continue

            # PART 1: Preday
            try:
                context['last_focus'] = user.focuses.get(scope=Scope.DAY.value, start=scope.start - timezone.timedelta(days=1))
            except Focus.DoesNotExist:
                pass

            # PART 2: Current day
            try:
                context['focus'] = user.focuses.get(scope=Scope.DAY.value, start=scope.start)
            except Focus.DoesNotExist:
                pass

            # REPORT
            subject = f"{user}'s focus report"
            message = render_to_string('office/emails/focus_report.txt', context)
            user.duo.notify_partners(user, subject, message)
            self.stdout.write(f'> Sent for {user}')

