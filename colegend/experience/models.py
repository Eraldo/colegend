from django.db import models
from django.db.models import Sum, Max
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


class ExperienceQuerySet(OwnedQuerySet):
    def total(self, app=None, level=None):
        queryset = self
        if app:
            queryset = queryset.filter(app=app)
        if level is not None:
            queryset = queryset.filter(level=level)
        return queryset.aggregate(Sum('amount')).get('amount__sum') or 0

    def level(self, app=JOURNEY):
        return self.filter(app=app).aggregate(Max('level')).get('level__max') or 0


class Experience(OwnedBase, TimeStampedBase):
    app = models.CharField(
        _('app'),
        choices=APP_CHOICES,
        max_length=10,
    )
    level = models.IntegerField(
        verbose_name=_('level'),
    )
    amount = models.IntegerField(
        verbose_name=_('amount'),
    )

    objects = ExperienceQuerySet.as_manager()

    class Meta:
        default_related_name = 'experience'

    def __str__(self):
        return '{amount} EXP {app}#{level} ({owner})'.format(
            owner=self.owner, amount=self.amount, app=self.app, level=self.level
        )


def add_experience(user, app, amount):
    level = Experience.objects.level(app)
    amount = 1
    return user.experience.create(owner=user, app=app, level=level, amount=amount)
