from django.db import models
from django.db.models import Sum
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from colegend.core.models import OwnedBase, TimeStampedBase, OwnedQuerySet

HOME = 'home'
ARCADE = 'arcade'
OFFICE = 'office'
COMMUNITY = 'community'
STUDIO = 'studio'
ACADEMY = 'academy'
JOURNEY = 'journey'
APP_CHOICES = (
    (HOME, _('home')),
    (ARCADE, _('arcade')),
    (OFFICE, _('office')),
    (COMMUNITY, _('community')),
    (STUDIO, _('studio')),
    (ACADEMY, _('academy')),
    (JOURNEY, _('journey')),
)

ACTION_CHOICES = APP_CHOICES


class ExperienceQuerySet(OwnedQuerySet):
    def total(self, action=None, level=None):
        queryset = self
        if action:
            queryset = queryset.filter(action=action)
        if level is not None:
            # TODO: Subtract experience below selected level.
            pass
        return queryset.aggregate(Sum('amount')).get('amount__sum') or 0

    def level(self):
        # TODO: Implement level calculation. (or use table)
        # Workaround: Levelup every 100 exp.
        experience = self.total() or 0
        level = int(experience / 100)
        return level


class Experience(OwnedBase, TimeStampedBase):
    action = models.CharField(
        _('action'),
        choices=ACTION_CHOICES,
        max_length=100,
    )
    amount = models.IntegerField(
        verbose_name=_('amount'),
    )

    objects = ExperienceQuerySet.as_manager()

    class Meta:
        default_related_name = 'experience'

    def __str__(self):
        return '{amount} EXP {action} ({owner})'.format(
            owner=self.owner, amount=self.amount, action=self.action
        )


def add_experience(user, action, amount=1):
    # Daily experience caps:
    today = timezone.localtime(timezone.now()).date()
    app_exp_today = user.experience.filter(action=action, created__date=today).count()
    if app_exp_today <= 4:
        return user.experience.create(owner=user, action=action, amount=amount)
