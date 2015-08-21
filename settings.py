import sys
from path import path
from os.path import dirname, abspath

PROJ_ROOT = path(dirname(abspath(__file__)))
PROJ_NAME = PROJ_ROOT.name
APPS_ROOT = PROJ_ROOT/'apps'

sys.path.insert(0, APPS_ROOT)

SECRET_KEY = '%8gym4g0s4)vf5a6l%!g9&$#lb-c26o=u-dzuic6s3d9yt&6+l'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'crispy_forms',
    'django_extensions',
    'djcelery',
    'kombu.transport.django',

    'main',
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

ROOT_URLCONF = 'urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'main.context_processors.g',
            ],
        },
    },
]

WSGI_APPLICATION = 'wsgi.application'

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
        'NAME': 'main',
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'mysql',
        'PORT': '3306',
    },
}

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    PROJ_ROOT/'static',
)

WWW_ROOT = PROJ_ROOT/'www'
STATIC_ROOT = WWW_ROOT/'static'
MEDIA_ROOT = WWW_ROOT/'media'

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

# Celery
import djcelery
djcelery.setup_loader()

BROKER_URL = 'django://'

from datetime import timedelta

CELERYBEAT_SCHEDULE = {
    'refresh-tokens': {
        'task': 'main.tasks.demo',
        'schedule': timedelta(seconds=60),
    },
}

CRISPY_TEMPLATE_PACK = 'bootstrap3'

SITE_URL = 'http://localhost:8000'