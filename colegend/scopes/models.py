from enum import Enum

from django.db import models
from django.utils.translation import ugettext_lazy as _

from colegend.journals.scopes import Day, Week, Month, Year


class Scope(Enum):
    DAY = 'day'
    WEEK = 'week'
    MONTH = 'month'
    YEAR = 'year'

    @staticmethod
    def get_choices():
        return [(scope.value, _(scope.value)) for scope in Scope]

    @staticmethod
    def get_values():
        return [scope.value for scope in Scope]

    @staticmethod
    def get_above(scope):
        scopes = Scope.get_values()
        return scopes[scopes.index(scope)+1:]

    @staticmethod
    def get_below(scope):
        scopes = Scope.get_values()
        return scopes[:scopes.index(scope)]


class ScopeField(models.CharField):
    description = _("Time scope (day/week/month/year)")

    def __init__(self, *args, **kwargs):
        verbose_name = kwargs.pop('verbose_name', _('scope'))
        choices = kwargs.pop('choices', Scope.get_choices())
        default = kwargs.pop('default', Scope.DAY.value)
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
        Scope.DAY.value: Day,
        Scope.WEEK.value: Week,
        Scope.MONTH.value: Month,
        Scope.YEAR.value: Year,
    }
    return scope_map.get(name)
