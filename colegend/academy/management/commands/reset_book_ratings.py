from django.core.management.base import BaseCommand
from django.utils import timezone

from colegend.academy.models import Book


class Command(BaseCommand):
    help = 'Reset book ratings'

    def handle(self, *args, **options):
        self.process()

    def process(self):
        """
        Calculate the book ratings for each book based on its review rating average and update the book rating.
        """
        for book in Book.objects.all():
            old = book.rating
            book.update_rating()
            new = book.rating
            if old != new:
                book.save(update_fields=['rating'])
                self.stdout.write(f'[{book}] {old} => {new}')
