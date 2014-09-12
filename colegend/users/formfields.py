from floppyforms import BooleanField
from applications.validators import validate_checked

__author__ = 'eraldo'


class RequiredBoolean(BooleanField):
    default_validators = [validate_checked]
