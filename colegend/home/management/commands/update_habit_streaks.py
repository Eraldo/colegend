import logging

from django.core.management.base import BaseCommand
from colegend.home.tasks import update_habit_streaks

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Updates habit streaks'

    def handle(self, *args, **options):
        verbosity = int(options['verbosity'])
        root_logger = logging.getLogger('')
        if verbosity > 1:
            root_logger.setLevel(logging.DEBUG)

        update_habit_streaks()
