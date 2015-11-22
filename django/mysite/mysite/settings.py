"""
Django settings for mysite project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os


BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'za2^mas^l+p%62a2av6lcd&8k9-8e5hj=idl!z6@qpsmok4eq3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

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
    'mysite.apps.notes',
    'mysite.apps.photofolio',
    'mysite.mytemplates',
    #'haystack',

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
)

ROOT_URLCONF = 'mysite.urls'

#'mysite.apps.notes.urls'

WSGI_APPLICATION = 'mysite.wsgi.application'


#mysql -u root
#GRANT ALL PRIVILEGES ON *.* TO 'webdev'@'localhost' IDENTIFIED BY 'webdev' WITH GRANT OPTION;
#mysql -p

# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    'default': {
            'ENGINE': 'django.db.backends.mysql', 
        	'NAME': 'notedb',
	        'USER': 'webdev',
        	'PASSWORD': 'webdev',
	        'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
        	'PORT': '3306'
    }
}

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/
#MEDIA_URL = ''
#MEDIA_ROOT = '/static/'
#PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
STATIC_URL = '/static/'
#STATIC_ROOT = os.path.join(PROJECT_PATH,'static')
#STATIC_ROOT = os.path.join(PROJECT_PATH, '..', 'static')

 #STATICFILES_FINDERS = (
 #   'django.contrib.staticfiles.finders.FileSystemFinder',
 #   'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#)


TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__), 'templates').replace('\\','/'),
    #'/home/webdev/work/django/mysite/mysite/templates',
)