from floppyforms import BooleanField
from users.validators import validate_checked

__author__ = 'eraldo'


class RequiredBoolean(BooleanField):
    default_validators = [validate_checked]
