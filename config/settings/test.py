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

# Used to find base.test template to extend it.
INSTALLED_APPS += ('tests',)
