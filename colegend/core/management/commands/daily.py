from django.core.management.base import BaseCommand
from django.utils import timezone

from colegend.journals.models import JournalEntry, Journal
from colegend.scopes.models import Scope
from colegend.users.models import User


class Command(BaseCommand):
    help = 'Handles daily tasks'

    def handle(self, *args, **options):
        self.process_streaks()

    def process_streaks(self):
        """
        Check if the user's streaks have been kept up.
        Is supposed to run after midnight. (Hence the preday date check.)
        """

        date = timezone.localtime(timezone.now()).date()
        self.stdout.write(f'# Checking journal streaks for {date}')

        # Looking only at journals with an active streak and get their users.
        active_journals = Journal.objects.exclude(streak=0)
        streak_user_pks = active_journals.values_list('owner', flat=True)

        # Yesterday's journal dayentries.
        entries = JournalEntry.objects.filter(scope=Scope.DAY.value, start=date - timezone.timedelta(days=1), owner__in=streak_user_pks)

        # Users who did write their entry.
        writer_ids = entries.values_list('owner', flat=True)

        for user in User.objects.filter(pk__in=streak_user_pks, is_active=True):
            streak = user.journal.streak
            # TODO: Checking if he wrote his journal day entry.
            if streak and user.pk not in writer_ids:
                # Resetting streak. :|
                user.journal.streak = 0
                user.journal.save()
                message = f'[{user}] Reset streak from {streak} to 0'
                self.stdout.write(message)
