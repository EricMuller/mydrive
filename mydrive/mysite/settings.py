"""
Django settings for mysite project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import djcelery
import os
import socket
import sys

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

PROJECT_DIR = os.path.dirname(os.path.realpath(__file__))
ROOT_DIR = os.path.dirname(PROJECT_DIR)
APPS_DIR = os.path.realpath(os.path.join(ROOT_DIR, 'apps'))
sys.path.append(APPS_DIR)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'za2^mas^l+p%62a2av6lcd&8k9-8e5hj=idl!z6@qpsmok4eq3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


if socket.gethostname().find('.') >= 0:
    HOSTNAME = socket.gethostname()
else:
    HOSTNAME = socket.gethostbyaddr(socket.gethostname())[0]

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '192.168.0.100', '0.0.0.0']

# logging

LOGGING = {
    'disable_existing_loggers': False,
    'version': 1,
    'handlers': {
        'console': {
            # logging handler that outputs log messages to terminal
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',  # message level to be written to console
        },
    },
    'loggers': {
        '': {
            # this sets root level logger to log debug and higher level
            # logs to console. All other loggers inherit settings from
            # root level logger.
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,  # this tells logger to send logging message
            # to its parent (will send if set to True)
        },
        'django.db': {
            # django also has database level logging
            'level': 'DEBUG',
            'handers': ['console'],
        },
        'django.db.backends': {
            'level': 'DEBUG',
            'handers': ['console'],
        },
        'django.db.backends.schema': {
            'propagate': False,  # don't log schema queries, django >= 1.7
        },
        'ged.services.folders': {
            'level': 'DEBUG',
            'handers': ['console'],
        },
    },
}

# Application definition

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': os.path.join(os.path.dirname(__file__), 'whoosh_index'),
    },
}

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'channels',
    # 'swampdragon',
    'drive',
    'mydrive',
    'rest_framework_swagger',
    'djcelery',
    # 'kombu.transport.django',  # django dtatbase
    # 'haystack',
    # 'debug_toolbar',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    # 'debug_toolbar.middleware.DebugToolbarMiddleware',
    # 'django.middleware.transaction.TransactionMiddleware',
)

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',
    ),
    'DEFAULT_PAGINATION_CLASS':
    'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 100,
    # 'DEFAULT_PERMISSION_CLASSES': (
    #    'rest_framework.permissions.AllowAny',
    #    'rest_framework.permissions.DjangoModelPermissions',
    # ),
}

ROOT_URLCONF = 'mysite.urls'

# 'mysite.apps.notes.urls'
WSGI_APPLICATION = 'mysite.wsgi.application'

# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases
if HOSTNAME == 'localhost':
    STATIC_ROOT = '/var/www/html/static'
    MEDIA_ROOT = '/home/webdev/tmp/'
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'mydrive',
            'USER': 'webdev',
            'PASSWORD': 'webdev',
            'HOST': '192.168.100',  # Or an IP DB Address
            'PORT': '3306'
        }
    }
else:
    # could9
    STATIC_ROOT = 'static'
    MEDIA_ROOT = '/home/ubuntu/tmp/'
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'c9',
            'USER': 'eric_muller',
            'PASSWORD': '',
            'HOST': '0.0.0.0',  # Or an IP DB Address
            'PORT': '3306'
        }
    }

# print(DATABASES)
# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# upload files
MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/
# for collectstatic

STATIC_URL = '/static/'


STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'handlers.custom_exception_handler'
}

SWAMP_DRAGON_CONNECTION = (
    'swampdragon.connections.sockjs_connection.DjangoSubscriberConnection',
    '/data')

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "asgiref.inmemory.ChannelLayer",
        "ROUTING": "mysite.routing.channel_routing",
    },
}

# STATICFILES_DIRS = [
# os.path.join(BASE_DIR, "static"),
# ]

TEST_RUNNER = 'django.test.runner.DiscoverRunner'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'mysite/templates').replace('\\', '/')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # Insert your TEMPLATE_CONTEXT_PROCESSORS here or use this
                # list if you haven't customized them:
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
            'debug': True,
        },
    },
]

# TEMPLATE_DIRS = (
# os.path.join(os.path.dirname(__file__), '/templates').replace('\\', '/'),
# os.path.join(PROJECT_PATH, 'templates/')
# '/home/webdev/work/django/mysite/mysite/templates',
# )

# TEMPLATE_DEBUG = True

SWAGGER_SETTINGS = {
    'exclude_namespaces': ['internal_apis'],
    'api_version': '0.1',
    'api_path': '/',
    'enabled_methods': [
        'get',
        'post',
        'put',
        # 'patch',
        'delete'
    ],
    'api_key': '',
    'is_authenticated': False,
    'is_superuser': False,
    'unauthenticated_user': 'django.contrib.auth.models.AnonymousUser',
    'permission_denied_handler': None,
    'resource_access_handler': None,
    # 'base_path': 'helloreverb.com/docs',
    'info': {
        'contact': 'e.mul@free.fr',
        'description': 'This is my drive REST API. ',
        'license': 'Apache 2.0',
        'licenseUrl': 'http://www.apache.org/licenses/LICENSE-2.0.html',
        'termsOfServiceUrl': 'http://helloreverb.com/terms/',
        'title': 'My drive REST API',
    },
    'doc_expansion': 'none',
}

# Celery
# https://www.caktusgroup.com/blog/2014/06/23/scheduling-tasks-celery/
# http://docs.celeryproject.org/en/latest/configuration.html#conf-broker-settings
djcelery.setup_loader()
# BROKER_URL = 'django://'
#BROKER_URL = 'amqp://guest:guest@centos:5672//'

BROKER_URL = 'amqp://mydrive:mydrive@centos:5672/centos'


