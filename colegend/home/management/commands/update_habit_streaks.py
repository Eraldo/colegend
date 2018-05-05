from django.core.management.base import BaseCommand
from django.utils import timezone

from colegend.home.models import Habit


class Command(BaseCommand):
    help = 'Updates habit streaks'

    def handle(self, *args, **options):
        """
        Check if the user's streaks have been kept up.
        Is supposed to run after midnight. (Hence the preday date check.)
        """

        date = timezone.localtime(timezone.now()).date()
        self.stdout.write(f'# Checking habit streaks for {date}')

        # Looking only at habits with an active streak and getting their users.
        habits = Habit.objects.exclude(streak=0)

        # TODO: Finding more efficient strategy for bulk processing below.
        # Solution idea 1: One query per scope.
        # Solution idea 2: Other idea, check:
        # Every day: DAY habits
        # On Monday: also WEEK habits
        # first of Month: MONTH habits
        # On first of year: YEAR habits

        # Checking if streak chain is still ok.
        yesterday = date - timezone.timedelta(days=1)
        for habit in habits:
            if habit.check_streak(yesterday):
                continue
            else:
                habit.reset_streak()
                message = f'[{habit.owner}] Reset streak for habit #{habit.id}: {habit}'
                self.stdout.write(message)
