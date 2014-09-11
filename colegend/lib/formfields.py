from floppyforms import CharField
from lib.validators import PhoneValidator

__author__ = 'eraldo'


class PhoneField(CharField):
    default_validators = [PhoneValidator()]

    def __init__(self, *args, **kwargs):
        super(PhoneField, self).__init__(*args, min_length=10, max_length=16, **kwargs)
