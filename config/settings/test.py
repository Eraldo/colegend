# -*- coding: utf-8 -*-
'''
Test settings
'''

# noinspection PyUnresolvedReferences
from .local import *  # noqa

# Mail settings
# ------------------------------------------------------------------------------
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025
