from enum import Enum

from django.db import models
from django.utils.translation import ugettext_lazy as _

from colegend.journals.scopes import Day, Week, Month, Year


class Scope(Enum):
    DAY = 'day'
    WEEK = 'week'
    MONTH = 'month'
    YEAR = 'year'


DAY = 'day'
WEEK = 'week'
MONTH = 'month'
QUARTER = 'quarter'
YEAR = 'year'
SCOPE_CHOICES = (
    (DAY, _('day')),
    (WEEK, _('week')),
    (MONTH, _('month')),
    (YEAR, _('year')),
)


class ScopeField(models.CharField):
    description = _("Time scope (day/week/month/year)")

    def __init__(self, *args, **kwargs):
        verbose_name = kwargs.pop('verbose_name', _('scope'))
        choices = kwargs.pop('choices', SCOPE_CHOICES)
        default = kwargs.pop('default', DAY)
        max_length = kwargs.pop('max_length', 5)
        super().__init__(
            verbose_name=verbose_name,
            choices=choices,
            default=default,
            max_length=max_length,
            *args, **kwargs
        )


def get_scope_by_name(name):
    scope_map = {
        DAY: Day,
        WEEK: Week,
        MONTH: Month,
        YEAR: Year,
    }
    return scope_map.get(name)
