# -*- coding: utf-8 -*-
"""
Django settings for coLegend project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""
import environ

ROOT_DIR = environ.Path(__file__) - 3  # (/a/b/myfile.py - 3 = /)
APPS_DIR = ROOT_DIR.path('colegend')

env = environ.Env()

READ_DOT_ENV_FILE = env.bool('DJANGO_READ_DOT_ENV_FILE', default=True)
if READ_DOT_ENV_FILE:
    # OS environment variables take precedence over variables from .env
    ENV_FILE = ROOT_DIR.path('.env')
    if environ.os.path.isfile(str(ENV_FILE)):
        env.read_env(str(ENV_FILE))

# GENERAL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = env.bool('DJANGO_DEBUG', False)
# Local time zone. Choices are
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# though not all of them may be available with every OS.
# In Windows, this must be set to your system time zone.
TIME_ZONE = 'Europe/Berlin'
# https://docs.djangoproject.com/en/dev/ref/settings/#language-code
LANGUAGE_CODE = 'en'
# https://docs.djangoproject.com/en/dev/ref/settings/#site-id
SITE_ID = 1
# https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
USE_I18N = True
# https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
USE_L10N = True
# https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
USE_TZ = True

# DATABASES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': env.db("DATABASE_URL", default="postgres:///colegend"),
}
DATABASES['default']['ATOMIC_REQUESTS'] = True

# URLS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#root-urlconf
ROOT_URLCONF = 'config.urls'
# https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = 'config.wsgi.application'

# APPS
# ------------------------------------------------------------------------------
DJANGO_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'django.contrib.humanize', # Handy template tags
    'django.contrib.admin',
]
THIRD_PARTY_APPS = [
    'crispy_forms',  # Form layouts
    'allauth',  # registration
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.facebook',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_auth',
    'rest_auth.registration',
    'graphene_django',
    # 'django_gravatar', # TODO: Researching if this is still in the project?
    'ordered_model',
    'simplemde',
    'dal',
    'dal_select2',
    'easy_thumbnails',
    'django_filters',
    'django_countries',
]
LOCAL_APPS = [
    # 'colegend.users',  # custom users ('legends') app
    'colegend.users.apps.UsersConfig',
    # Your stuff: custom apps go here
    # General
    'colegend.checkpoints',
    'colegend.roles',
    'colegend.donations',
    'colegend.experience',
    'colegend.core',  # common code library
    'colegend.categories',
    'colegend.tags',
    'colegend.cms',
    'colegend.crm',
    'colegend.components',
    'colegend.coicons',
    'colegend.api',
    # Website
    'colegend.about',
    'colegend.welcome',
    # Main apps
    'colegend.home',
    'colegend.arcade',
    'colegend.office',
    'colegend.community',
    'colegend.studio',
    'colegend.academy',
    'colegend.journey',
    # Project apps
    'colegend.support',
    'colegend.blog',
    'colegend.resources',
    'colegend.news',
    # Studio
    'colegend.journals',
    # Manager
    'colegend.manager',
    'colegend.outcomes',
    'colegend.visions',
    # Community
    'colegend.events',
    'colegend.guidelines',
    'colegend.chat',
    'colegend.guides',
    # Journey
    'colegend.tutorials',
    'colegend.outercall',
    'colegend.innercall',
    'colegend.biography',
    # Misc
    'colegend.mockups',
    'colegend.styleguide',
    'colegend.metrics',
    'colegend.sandbox',
    'colegend.lab',
]
CMS_APPS = [
    'wagtail.contrib.forms',
    'wagtail.contrib.redirects',
    'wagtail.embeds',
    'wagtail.sites',
    'wagtail.users',
    'wagtail.snippets',
    'wagtail.documents',
    'wagtail.images',
    'wagtail.search',
    'wagtail.admin',
    'wagtail.core',
    'wagtail.contrib.routable_page',

    'taggit',
    'modelcluster',
]
# https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + CMS_APPS + LOCAL_APPS

# MIGRATIONS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#migration-modules
MIGRATION_MODULES = {
    'sites': 'colegend.contrib.sites.migrations',
}

# AUTHENTICATION
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#authentication-backends
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-user-model
AUTH_USER_MODEL = 'users.User'
# https://docs.djangoproject.com/en/dev/ref/settings/#login-redirect-url
LOGIN_REDIRECT_URL = '/'
# https://docs.djangoproject.com/en/dev/ref/settings/#login-url
LOGIN_URL = '/welcome/'

# PASSWORDS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#password-hashers
PASSWORD_HASHERS = [
    # https://docs.djangoproject.com/en/dev/topics/auth/passwords/#using-argon2-with-django
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
]
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# MIDDLEWARE
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # custom
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    # wagtail cms
    'wagtail.core.middleware.SiteMiddleware',
    'wagtail.contrib.redirects.middleware.RedirectMiddleware',
]

# STATIC
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = env('STATIC_ROOT', default=str(ROOT_DIR('staticfiles')))
# https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = '/static/'
# https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = [
    str(APPS_DIR.path('static')),
]
# https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

# MEDIA
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = str(ROOT_DIR('media'))
# https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = '/media/'

# TEMPLATES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#templates
TEMPLATES = [
    {
        # https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-TEMPLATES-BACKEND
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
        'DIRS': [
            str(APPS_DIR.path('templates')),
        ],
        'OPTIONS': {
            # https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
            'debug': DEBUG,
            # https://docs.djangoproject.com/en/dev/ref/settings/#template-loaders
            # https://docs.djangoproject.com/en/dev/ref/templates/api/#loader-types
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
            # https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
# http://django-crispy-forms.readthedocs.io/en/latest/install.html#template-packs
CRISPY_TEMPLATE_PACK = 'bootstrap4'

# FIXTURES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#fixture-dirs
FIXTURE_DIRS = (
    str(APPS_DIR.path('fixtures')),
)

# EMAIL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = env('DJANGO_EMAIL_BACKEND', default='django.core.mail.backends.smtp.EmailBackend')

# ADMIN
# ------------------------------------------------------------------------------
# Django Admin URL regex.
ADMIN_URL = env('DJANGO_ADMIN_URL', default=r'^admin/')
# https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = [
    ("""Eraldo Energy""", 'eraldo@eraldo.org'),
]
# https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS

# Celery
# ------------------------------------------------------------------------------
INSTALLED_APPS += ['colegend.taskapp.celery.CeleryConfig']
# http://docs.celeryproject.org/en/latest/userguide/configuration.html#std:setting-broker_url
CELERY_BROKER_URL = env('CELERY_BROKER_URL', default='django://')
# http://docs.celeryproject.org/en/latest/userguide/configuration.html#std:setting-result_backend
if CELERY_BROKER_URL == 'django://':
    CELERY_RESULT_BACKEND = 'redis://'
else:
    CELERY_RESULT_BACKEND = CELERY_BROKER_URL
# http://docs.celeryproject.org/en/latest/userguide/configuration.html#std:setting-accept_content
CELERY_ACCEPT_CONTENT = ['json']
# http://docs.celeryproject.org/en/latest/userguide/configuration.html#std:setting-task_serializer
CELERY_TASK_SERIALIZER = 'json'
# http://docs.celeryproject.org/en/latest/userguide/configuration.html#std:setting-result_serializer
CELERY_RESULT_SERIALIZER = 'json'

# django-allauth
# ------------------------------------------------------------------------------
ACCOUNT_ALLOW_REGISTRATION = env.bool('DJANGO_ACCOUNT_ALLOW_REGISTRATION', True)
# https://django-allauth.readthedocs.io/en/latest/configuration.html
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
# https://django-allauth.readthedocs.io/en/latest/configuration.html
ACCOUNT_EMAIL_REQUIRED = True
# https://django-allauth.readthedocs.io/en/latest/configuration.html
ACCOUNT_EMAIL_VERIFICATION = 'optional'
# https://django-allauth.readthedocs.io/en/latest/configuration.html
ACCOUNT_ADAPTER = 'colegend.users.adapters.AccountAdapter'
# https://django-allauth.readthedocs.io/en/latest/configuration.html
SOCIALACCOUNT_ADAPTER = 'colegend.users.adapters.SocialAccountAdapter'
# https://django-allauth.readthedocs.io/en/latest/configuration.html
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = False
# https://django-allauth.readthedocs.io/en/latest/configuration.html
ACCOUNT_USERNAME_MIN_LENGTH = 4
# https://django-allauth.readthedocs.io/en/latest/configuration.html
ACCOUNT_SESSION_REMEMBER = True
# https://django-allauth.readthedocs.io/en/latest/configuration.html
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True
# Custom provider settings
GOOGLE_ID = env('GOOGLE_ID')
GOOGLE_KEY = env('GOOGLE_KEY')
FACEBOOK_ID = env('FACEBOOK_ID')
FACEBOOK_KEY = env('FACEBOOK_KEY')

# Custom base stuff:
# ------------------------------------------------------------------------------

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

# CMS - WATAIL CMS
# ------------------------------------------------------------------------------
BASE_URL = env('BASE_URL', default=None)  # used by wagtailadmin notifications
WAGTAIL_SITE_NAME = 'coLegend'
WAGTAILIMAGES_MAX_UPLOAD_SIZE = 1 * 1024 * 1024  # Example: `20 * 1024 * 1024` => 20MB
WAGTAILADMIN_NOTIFICATION_USE_HTML = True
TAGGIT_CASE_INSENSITIVE = True
# WAGTAILADMIN_NOTIFICATION_FROM_EMAIL = 'connect@coLegend.org'
# PASSWORD_REQUIRED_TEMPLATE = 'myapp/password_required.html'
# WAGTAIL_USER_EDIT_FORM = 'users.forms.CustomUserEditForm'
# WAGTAIL_USER_CREATION_FORM = 'users.forms.CustomUserCreationForm'
# WAGTAIL_USER_CUSTOM_FIELDS = ['country']
# WAGTAIL_USAGE_COUNT_ENABLED = True


# API - django rest framework (DRF)
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

# API - graphene django
# ------------------------------------------------------------------------------
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
    'app.colegend.org',
    'app.colegend.com',  # .com to be removed
    'staging.colegend.org',
    'staging.colegend.com',  # .com to be removed
    'localhost:8100',
)
# CORS_ORIGIN_REGEX_WHITELIST = (
#     r'^(https?://)?(\w+\.)?colegend\.(org|com)$',
#     r'^(https?://)?(\w+\.)?127\.0\.0\.1:8004$',
# )


# SLACK - django-slack
# ------------------------------------------------------------------------------
INSTALLED_APPS += ['django_slack']
SLACK_TOKEN = env('SLACK_TOKEN', default=None)
SLACK_CHANNEL = env("SLACK_CHANNEL", default='core')
SLACK_USERNAME = 'colegend'
SLACK_ICON_EMOJI = ':co:'
SLACK_TEAM_ID = 'colegend'

# django-simplemde
# ------------------------------------------------------------------------------
SIMPLEMDE_OPTIONS = {
    'indentWithTabs': False,
    'autosave': {
        'enabled': True,
        'delay': 60000,
    },
    'tabSize': 4,
    'spellChecker': False,
}

# django-extensions
# ------------------------------------------------------------------------------
# https://django-extensions.readthedocs.io/en/latest/installation_instructions.html#configuration
INSTALLED_APPS += ['django_extensions']
