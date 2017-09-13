# -*- coding: utf-8 -*-
"""
Django settings for coLegend project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""
from __future__ import absolute_import, unicode_literals

import environ

ROOT_DIR = environ.Path(__file__) - 3  # (/a/b/myfile.py - 3 = /)
APPS_DIR = ROOT_DIR.path('colegend')

env = environ.Env()
env_file = ROOT_DIR('.env')
if environ.os.path.isfile(env_file):
    env.read_env(env_file)

# APP CONFIGURATION
# ------------------------------------------------------------------------------
DJANGO_APPS = (
    # Default Django apps:
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Useful template tags:
    # 'django.contrib.humanize',

    # Admin
    'django.contrib.admin',

    'colegend.users',  # custom users ('legends') app
)

CMS_APPS = (
    'wagtail.wagtailforms',
    'wagtail.wagtailredirects',
    'wagtail.wagtailembeds',
    'wagtail.wagtailsites',
    'wagtail.wagtailusers',
    'wagtail.wagtailsnippets',
    'wagtail.wagtaildocs',
    'wagtail.wagtailimages',
    'wagtail.wagtailsearch',
    'wagtail.wagtailadmin',
    'wagtail.wagtailcore',

    'wagtail.contrib.wagtailroutablepage',

    'taggit',
    'modelcluster',
)

THIRD_PARTY_APPS = (
    'crispy_forms',  # Form layouts
    'allauth',  # registration
    'allauth.account',  # registration
    'allauth.socialaccount',  # registration
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.facebook',
    'django_gravatar', # TODO: Researching if this is still in the project?
    'orderable',
    'simplemde',
    'dal',
    'dal_select2',
    'easy_thumbnails',
    'django_filters',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_auth',
    'rest_auth.registration',
    'graphene_django',
)

# Apps specific for this project go here.
LOCAL_APPS = (
    # Your stuff: custom apps go here
    'colegend.checkpoints',
    'colegend.roles',
    'colegend.donations',
    'colegend.experience',

    'colegend.core',  # common code library
    'colegend.about',
    'colegend.welcome',

    # main apps
    'colegend.home',
    'colegend.arcade',
    'colegend.office',
    'colegend.community',
    'colegend.studio',
    'colegend.academy',
    'colegend.journey',

    'colegend.support',
    'colegend.blog',
    'colegend.resources',
    'colegend.news',

    # common
    'colegend.categories',
    'colegend.tags',

    # Studio
    'colegend.journals',

    # Manager
    'colegend.manager',
    'colegend.outcomes',

    'colegend.visions',

    'colegend.guidelines',
    'colegend.chat',
    'colegend.outercall',
    'colegend.innercall',
    'colegend.biography',
    'colegend.guides',
    'colegend.events',

    'colegend.games',
    'colegend.cards',
    'colegend.story',

    'colegend.mockups',
    'colegend.styleguide',
    'colegend.metrics',

    'colegend.sandbox',

    'colegend.cms',
    'colegend.components',
    'colegend.coicons',
    'colegend.api',
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + CMS_APPS + THIRD_PARTY_APPS

# MIDDLEWARE CONFIGURATION
# ------------------------------------------------------------------------------
MIDDLEWARE_CLASSES = (
    # Make sure djangosecure.middleware.SecurityMiddleware is listed first
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    # wagtail cms
    'wagtail.wagtailcore.middleware.SiteMiddleware',
    'wagtail.wagtailredirects.middleware.RedirectMiddleware',
)

# MIGRATIONS CONFIGURATION
# ------------------------------------------------------------------------------
MIGRATION_MODULES = {
    'sites': 'colegend.contrib.sites.migrations',
}

# DEBUG
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = env.bool("DJANGO_DEBUG", False)

# FIXTURE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-FIXTURE_DIRS
FIXTURE_DIRS = (
    str(APPS_DIR.path('fixtures')),
)

# EMAIL CONFIGURATION
# ------------------------------------------------------------------------------
EMAIL_BACKEND = env('DJANGO_EMAIL_BACKEND', default='django.core.mail.backends.smtp.EmailBackend')
DEFAULT_FROM_EMAIL = env('DJANGO_DEFAULT_FROM_EMAIL',
                         default='coLegend <connect@colegend.org>')
EMAIL_SUBJECT_PREFIX = env("DJANGO_EMAIL_SUBJECT_PREFIX", default='[coLegend] ')
SERVER_EMAIL = env('DJANGO_SERVER_EMAIL', default=DEFAULT_FROM_EMAIL)

# MANAGER CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = (
    ("""Eraldo Energy""", 'eraldo@eraldo.org'),
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS

# DATABASE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    # Raises ImproperlyConfigured exception if DATABASE_URL not in os.environ
    'default': env.db("DATABASE_URL", default="postgres:///colegend"),
}
DATABASES['default']['ATOMIC_REQUESTS'] = True

# GENERAL CONFIGURATION
# ------------------------------------------------------------------------------
# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Europe/Berlin'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#language-code
LANGUAGE_CODE = 'en'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#site-id
SITE_ID = 1

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
USE_I18N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
USE_L10N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
USE_TZ = True

# TEMPLATE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#templates
TEMPLATES = [
    {
        # See: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-TEMPLATES-BACKEND
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
        'DIRS': [
            str(APPS_DIR.path('templates')),
        ],
        'OPTIONS': {
            # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
            'debug': DEBUG,
            # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-loaders
            # https://docs.djangoproject.com/en/dev/ref/templates/api/#loader-types
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
            # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                # Your stuff: custom template context processors go here
            ],
        },
    },
]

# See: http://django-crispy-forms.readthedocs.org/en/latest/install.html#template-packs
CRISPY_TEMPLATE_PACK = 'bootstrap3'

# STATIC FILE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = str(ROOT_DIR('staticfiles'))

# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = '/static/'

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = (
    str(APPS_DIR.path('static')),
)

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# MEDIA CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = str(ROOT_DIR('media'))

# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = '/media/'

# URL Configuration
# ------------------------------------------------------------------------------
ROOT_URLCONF = 'config.urls'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = 'config.wsgi.application'

# AUTHENTICATION CONFIGURATION
# ------------------------------------------------------------------------------
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

# Some really nice defaults
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'optional'
ACCOUNT_SIGNUP_PASSWORD_VERIFICATION = False
ACCOUNT_USERNAME_MIN_LENGTH = 4
ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True
ACCOUNT_ADAPTER = 'colegend.users.adapters.AccountAdapter'
SOCIALACCOUNT_ADAPTER = 'colegend.users.adapters.SocialAccountAdapter'
ACCOUNT_ALLOW_REGISTRATION = env.bool("DJANGO_ACCOUNT_ALLOW_REGISTRATION", True)

# Custom user app defaults
# Select the correct user model
AUTH_USER_MODEL = 'users.User'
LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/welcome/'

# Provider settings
GOOGLE_ID = env('GOOGLE_ID')
GOOGLE_KEY = env('GOOGLE_KEY')
FACEBOOK_ID = env('FACEBOOK_ID')
FACEBOOK_KEY = env('FACEBOOK_KEY')

# SLUGLIFIER
AUTOSLUG_SLUGIFY_FUNCTION = 'slugify.slugify'

########## CELERY
INSTALLED_APPS += ('colegend.taskapp.celery.CeleryConfig',)
# if you are not using the django database broker (e.g. rabbitmq, redis, memcached), you can remove the next line.
INSTALLED_APPS += ('kombu.transport.django',)
BROKER_URL = env("CELERY_BROKER_URL", default='django://')
########## END CELERY


# Location of root django.contrib.admin URL, use {% url 'admin:index' %}
ADMIN_URL = env('DJANGO_ADMIN_URL', default='admin')

# Your common stuff: Below this line define 3rd party library settings


# EASY THUMBNAILS
# ------------------------------------------------------------------------------
THUMBNAIL_ALIASES = {
    '': {
        'small': {'size': (50, 50), 'crop': True},
        'medium': {'size': (100, 100), 'crop': True},
        'large': {'size': (200, 200), 'crop': True},
    },
}
THUMBNAIL_HIGH_RESOLUTION = True
THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'easy_thumbnails.processors.scale_and_crop',
    'easy_thumbnails.processors.filters',
)
THUMBNAIL_BASEDIR = 'thumbnails'


# WATAIL CMS
# ------------------------------------------------------------------------------
BASE_URL = env('BASE_URL', default=None)  # used by wagtailadmin notifications
WAGTAIL_SITE_NAME = 'coLegend'
WAGTAILIMAGES_MAX_UPLOAD_SIZE = 1 * 1024 * 1024 #  Example: `20 * 1024 * 1024` => 20MB
WAGTAILADMIN_NOTIFICATION_USE_HTML = True
TAGGIT_CASE_INSENSITIVE = True
# WAGTAILADMIN_NOTIFICATION_FROM_EMAIL = 'connect@colegend.org'
# PASSWORD_REQUIRED_TEMPLATE = 'myapp/password_required.html'
# WAGTAIL_USER_EDIT_FORM = 'users.forms.CustomUserEditForm'
# WAGTAIL_USER_CREATION_FORM = 'users.forms.CustomUserCreationForm'
# WAGTAIL_USER_CUSTOM_FIELDS = ['country']
# WAGTAIL_USAGE_COUNT_ENABLED = True


# API
# ------------------------------------------------------------------------------
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        # 'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ],
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        # 'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
        'rest_framework.permissions.IsAuthenticated'
        # 'rest_framework.permissions.IsAdminUser'
    ],
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
}
REST_AUTH_SERIALIZERS = {
    'USER_DETAILS_SERIALIZER': 'colegend.users.serializers.OwnedUserSerializer',
}
REST_AUTH_REGISTER_SERIALIZERS = {
    'REGISTER_SERIALIZER': 'colegend.users.serializers.JoinSerializer',
}

GRAPHENE = {
    'MIDDLEWARE': [
        'graphene_django.debug.DjangoDebugMiddleware',
        'colegend.api.middelware.AuthorizationMiddleware',
    ],
    'SCHEMA': 'colegend.api.schema.schema',
    'SCHEMA_OUTPUT': 'data/schema.json'  # defaults to schema.json
}
# CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST = (
    'localhost:8004',
    '127.0.0.1:8004',
    'colegend.org',
    'colegend.com',
    'app.colegend.com',
    'staging.colegend.com',
    'localhost:8100',
)
# CORS_ORIGIN_REGEX_WHITELIST = (
#     r'^(https?://)?(\w+\.)?colegend\.(org|com)$',
#     r'^(https?://)?(\w+\.)?127\.0\.0\.1:8004$',
# )


# SLACK CHAT
# ------------------------------------------------------------------------------
SLACK_TEAM_ID = 'colegend'


# SLACK IM
# ------------------------------------------------------------------------------
INSTALLED_APPS += ('django_slack',)
SLACK_TOKEN = env('SLACK_TOKEN', default=None)
SLACK_CHANNEL = env("SLACK_CHANNEL", default='core')
SLACK_BACKEND = 'django_slack.backends.Urllib2Backend'
SLACK_USERNAME = 'coLegend'
SLACK_ICON_EMOJI = ':co:'
SLACK_LINK_NAMES = '1'


SIMPLEMDE_OPTIONS = {
    'indentWithTabs': False,
    'autosave': {
        'enabled': True,
        'delay': 60000,
    },
    'tabSize': 4,
    'spellChecker': False,
}
