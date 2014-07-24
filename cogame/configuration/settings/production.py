"""Production settings and globals."""

__author__ = 'eraldo'


from os import environ

from .base import *

# Normally you should not import ANYTHING from Django directly
# into your settings, but ImproperlyConfigured is an exception.
from django.core.exceptions import ImproperlyConfigured

import json
local_settings_file = normpath(join(CONFIG_ROOT, 'settings', 'local_settings.json'))
with open(local_settings_file) as file:
    settings = json.loads(file.read())


def get_setting(setting, settings=settings, default=None, conversion_type=None):
    """ Get the environment setting or return exception """
    result = None
    # try to get it from the environment variables
    if setting in environ:
        result = environ.get(setting)

    # try to get it from a local json settings file
    try:
        result = settings[setting]
    except KeyError:
        if default:
            return default
        error_msg = "Set the %s env variable" % setting
        raise ImproperlyConfigured(error_msg)

    # convert to correct type if given
    if conversion_type:
        if conversion_type == bool:
                result = True if result == "True" else False
        elif conversion_type == int:
            try:
                result = int(result)
            except ValueError:
                error_msg = "The local variable %s was expected to be a string representing an integer" % setting
                raise ImproperlyConfigured(error_msg)
    return result


########## DEBUG CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = get_setting('DEBUG', default=False, conversion_type=bool)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
TEMPLATE_DEBUG = DEBUG
# http://david.feinzeig.com/blog/2012/02/18/
# tips-for-creating-404-page-not-found-and-500-server-error-templates-in-django-plus-configuring-email-alerts/
SEND_BROKEN_LINK_EMAILS = True
########## END DEBUG CONFIGURATION


########## HOST CONFIGURATION
# See: https://docs.djangoproject.com/en/1.5/releases/1.5/#allowed-hosts-required-in-production
ALLOWED_HOSTS = get_setting('ALLOWED_HOSTS', default=[])
USE_X_FORWARDED_HOST = get_setting('ALLOWED_HOSTS', default=False, conversion_type=bool)
########## END HOST CONFIGURATION


########## EMAIL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = get_setting('EMAIL_BACKEND', default='django.core.mail.backends.smtp.EmailBackend')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host
EMAIL_HOST = get_setting('EMAIL_HOST', default='smtp.gmail.com')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host-password
EMAIL_HOST_PASSWORD = get_setting('EMAIL_HOST_PASSWORD', default='-')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host-user
EMAIL_HOST_USER = get_setting('EMAIL_HOST_USER', default='your_email@example.com')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-port
EMAIL_PORT = get_setting('EMAIL_PORT', default=587)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-subject-prefix
EMAIL_SUBJECT_PREFIX = '[%s] ' % PROJECT_NAME

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-use-tls
EMAIL_USE_TLS = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#server-email
SERVER_EMAIL = EMAIL_HOST_USER
########## END EMAIL CONFIGURATION

########## DATABASE CONFIGURATION
# DATABASES = {}
########## END DATABASE CONFIGURATION


########## CACHE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
# CACHES = {}
########## END CACHE CONFIGURATION


########## SECRET CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = get_setting('SECRET_KEY')
########## END SECRET CONFIGURATION


########## MEDIA CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = get_setting('MEDIA_ROOT')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = '/media/'
########## END MEDIA CONFIGURATION


########## STATIC FILE CONFIGURATION
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = get_setting('STATIC_ROOT')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = '/static/'

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = (
    normpath(join(DJANGO_ROOT, 'static')),
)

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
########## END STATIC FILE CONFIGURATION


########## ADMIN CONFIGURATION
ADMIN_URL_BASE = r"^admin/"
########## END ADMIN CONFIGURATION


########## SECURITY CONFIGURATION
CSRF_COOKIE_SECURE = get_setting('CSRF_COOKIE_SECURE', default=True, conversion_type=bool)
SESSION_COOKIE_SECURE = get_setting('SESSION_COOKIE_SECURE', default=True, conversion_type=bool)
########## END SECURITY CONFIGURATION
