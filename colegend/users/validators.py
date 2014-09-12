from django.core.exceptions import ValidationError

__author__ = 'eraldo'


def validate_checked(value):
    """Used to make sure a BooleanField was checked upon submit."""
    if not value:
        raise ValidationError('Needs to be checked.')
