from django.core.management.base import BaseCommand
from django.utils import timezone

from colegend.users.models import User


class Command(BaseCommand):
    help = 'Handles monthly tasks'

    def handle(self, *args, **options):
        self.process_contribution()
        # self.compile_experience_report()

    def process_contribution(self):
        """Deduct the user chosen contribution amount from its balance"""
        self.stdout.write('# Contribution report {date}'.format(date=timezone.localtime(timezone.now()).date()))
        for user in User.objects.all():
            message = ''
            if user.is_active and user.is_premium:
                pre_balance = user.balance
                # Workaround amount. In the future maybe let the user decide an amount.
                amount = 42
                # Deduct credit from the user's balance.
                post_balance = pre_balance - amount
                user.balance = post_balance
                # Update the premium status if the balance is negative.
                if post_balance < 0:
                    user.is_premium = False
                user.save()
                message = '[{user} {active} {premium}] {pre_balance} - {amount} = {post_balance}'.format(
                    user=user,
                    active='Active' if user.is_active else 'Inactive',
                    premium='Premium' if user.is_premium else 'Free',
                    pre_balance=pre_balance, amount=amount, post_balance=post_balance
                )
            else:
                message = '[{user} {active} {premium}] {balance}'.format(
                    user=user,
                    active='Active' if user.is_active else 'Inactive',
                    premium='Premium' if user.is_premium else 'Free',
                    balance=user.balance
                )
            self.stdout.write(message)

    def compile_experience_report(self):
        """Create a report of how much experience each user gained in the previous month"""

        yesterday = timezone.localtime(timezone.now()) - timezone.timedelta(1)
        date = yesterday

        self.stdout.write('# Experience report for {year}-{month}'.format(year=yesterday.year, month=yesterday.month))
        for user in User.objects.all():
            experience = user.experience.filter(created__year=yesterday.year, created__month=yesterday.month).total()
            self.stdout.write('{user}: {experience}'.format(user=user, experience=experience))

    def hero_demon_update_reminder(self):
        """
        Remind the users to update their hero/demon if they have not been updated for a while (> 30 days).
        :return:
        """
        # TODO implement
        pass
