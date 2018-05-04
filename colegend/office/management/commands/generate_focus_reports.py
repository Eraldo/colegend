from django.core.mail import EmailMultiAlternatives
from django.core.management.base import BaseCommand
from django.template.loader import render_to_string
from django.utils import timezone

from colegend.community.models import Duo, Clan, Tribe
from colegend.scopes.models import Scope, get_scope_by_name
from colegend.users.models import User


class Community:
    name = 'Community'
    members = User.objects.all()


class Command(BaseCommand):
    help = 'Generates user focus reports'

    def add_arguments(self, parser):
        choices = [Scope.DAY.value, Scope.WEEK.value, Scope.MONTH.value, Scope.YEAR.value]
        parser.add_argument('scope', choices=choices)

    def handle(self, scope, *args, **options):
        """
        Check if the user's focus status and create a report for his partner(s).
        Is supposed to run after midday.

        General solution idea:
        1. Filtering: Only groups with at least one premium user.
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
        scope = get_scope_by_name(scope)(date=date)
        context = {'date': date, 'scope': scope}

        self.stdout.write(f'# Generating {scope.name} focus reports for {date}')

        # Get relevant groups.
        if scope.name == Scope.DAY.value:
            groups = Duo.objects.filter(members__is_premium=True).distinct()
        elif scope.name == Scope.WEEK.value:
            groups = Clan.objects.filter(members__is_premium=True).distinct()
        elif scope.name == Scope.MONTH.value:
            groups = Tribe.objects.filter(members__is_premium=True).distinct()
        elif scope.name == Scope.YEAR.value:
            groups = [Community]
        else:
            groups = []

        for group in groups:
            context['group'] = group

            subject = f"[{group.name}] {scope.name.title()} focus report: ({scope})"
            message = render_to_string('office/emails/focus_report.txt', context)

            emails = group.members.values_list('email', flat=True)
            email = EmailMultiAlternatives(subject=subject, body=message, to=emails, reply_to=emails)
            email.send()

            self.stdout.write(f'Sent for {group.name}')
