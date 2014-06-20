__author__ = 'eraldo'

from .base import *


DEBUG = True
TEMPLATE_DEBUG = DEBUG

INSTALLED_APPS += [
    'debug_toolbar',
]

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

FIXTURE_DIRS = (
    os.path.join(BASE_DIR, 'manager/fixtures/'),
)