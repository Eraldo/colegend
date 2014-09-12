from django.utils.translation import ugettext_lazy as _
from django.db.models import BooleanField
from users.validators import validate_checked

__author__ = 'eraldo'


class RequiredBooleanField(BooleanField):
    description = _("Boolean that needs to be True (Options:True/False)")

    default_validators = [validate_checked]

    def __init__(self, *args, **kwargs):
        super(RequiredBooleanField, self).__init__(*args, **kwargs)
