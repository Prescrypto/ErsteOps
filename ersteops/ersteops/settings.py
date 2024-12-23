"""
Django settings for ersteops project.

Generated by 'django-admin startproject' using Django 1.11.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
# Parse database configuration from $DATABASE_URL
import dj_database_url
# To transform strings from environment variables to boolean values
import ast
# decode redis URI
import urllib.parse

# redis_url=os.environ.get('REDIS_URL', 'redis://localhost:6379/0')
# # Parse the Redis URI
# url = urllib.parse.urlparse(redis_url)

# # Extract the host, port, and password
# redis_host = url.hostname
# redis_port = url.port
# redis_password = url.password


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = 'yzz21x+6-uhkx((v4p+7!u7p@kt&rm+ap&(wzd2hgi&m#zx7u1'
SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = True
DEBUG = ast.literal_eval(os.environ['DEBUG_STATE'])

# DEFAULT LOGIN URL
LOGIN_URL = '/'

# Django JET config
JET_SIDE_MENU_COMPACT = True

# TODO fix production mode
PRODUCTION = ast.literal_eval(os.environ['PRODUCTION'])
# Change allowed hosts accordingly
if PRODUCTION:
    ALLOWED_HOSTS = [os.environ['HEROKU_APP_NAME']+".herokuapp.com"]
else:
    # TODO Correct way
    # ALLOWED_HOSTS = [os.environ['ALLOWED_HOSTS']]
    ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    # django-jet
    'jet.dashboard',
    'jet',
    'rangefilter',
    'widget_tweaks',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'emergency.apps.EmergencyConfig',
    'notifications.apps.NotificationConfig',
    'preventconcurrentlogins',
    'channels',
    'home.apps.HomeConfig',
    'webpack_loader',
    'unit.apps.UnitConfig',
    'reports.apps.ReportsConfig',
    'paperless.apps.PaperlessConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'preventconcurrentlogins.middleware.PreventConcurrentLoginsMiddleware',
]

ROOT_URLCONF = 'ersteops.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        #'DIRS': [],
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'ersteops.processors.add_url_protocol',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'ersteops.wsgi.application'

APPEND_SLASH=False
#APPEND_SLASH=True
# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

# DATABASE CONFIG
DATABASE_URL = os.environ['DATABASE_URL']
DATABASES = {'default': dj_database_url.config(default=DATABASE_URL)}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'es-MX'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Secure Options
SECURE_SSL_REDIRECT = ast.literal_eval(os.environ['SECURE_SSL_REDIRECT'])
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Webpack loader for compiled front-end asserts
# https://github.com/ezhome/django-webpack-loader
WEBPACK_LOADER = {
    'DEFAULT': {
        'CACHE': not DEBUG,
        'BUNDLE_DIR_NAME': 'bundles/',
        'STATS_FILE': os.path.join(BASE_DIR, 'static/webpack-stats.json'),
    }
}

# Console logging for DEBUG=False - Probably should disable if DEBUG = True
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    "formatters": {
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        }
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'loggers': {
        'django_info': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        }
    },
}







"""
#Redis Cache
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": os.getenv('REDISTOGO_URL', 'redis://localhost:6379/0'),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "CONNECTION_POOL_KWARGS": {
                    # config for pool connections
                    "max_connections": 10
            }
        }
    }
}
# Redis Config
RQ_QUEUES = {
    'default': {
        'USE_REDIS_CACHE': 'default',
    },
    'high': {
        'USE_REDIS_CACHE': 'default',
    },
    'low': {
        'USE_REDIS_CACHE': 'default',
    }
}
# extra config args for RQ
RQ = {
    #RQ_EXCEPTION_HANDLERS = ['']
}
# CORS configuration
CORS_ORIGIN_ALLOW_ALL = True

"""

# Odoo api variables
BASE_URL = os.environ['BASE_URL']
ODOO_URL = os.environ['ODOO_URL']
ODOO_USERNAME = os.environ['ODOO_USERNAME']
ODOO_PASSWORD = os.environ['ODOO_PASSWORD']

# Google maps key
GEO_API_KEY = os.environ['GEO_API_KEY']

# Paperless URL
PAPERLESS_URL = os.environ['PAPERLESS_URL']

# Channels
ASGI_APPLICATION = 'ersteops.asgi.application'
#ASGI_APPLICATION = 'asgi.application'

#define channel layer
"""
Django channels funciona un a wsgi, ahora todas las peticiones llegan a una nueva capa
asgi "channels", para pruebas simples se puede usar runserver, para iniciar las capas
por separado se usa lo siguiente.
chanels(interface servers) ejemplo:
    daphne ersteops.asgi:channel_layer --port 8000 -b 0.0.0.0

worker (worker servers) ejemplo:
    python manage.py runworker

para mas informacion sobre el deployado o sus configuraciones
http://channels.readthedocs.io/en/latest/deploying.html
"""
#FIX_REDIS_URL = os.environ.get('REDIS_URL', 'redis://localhost:6379/0')+'/0?ssl_cert_reqs=CERT_NONE'
# os.environ.get('REDIS_TLS_URL', 'redis://localhost:6379/0')

CHANNEL_LAYERS = {
    "default": {
        #"BACKEND": "asgi_redis.RedisChannelLayer",
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [os.environ.get('REDIS_URL', 'redis://localhost:6379/0')],
            # "ssl": True,
            # "ssl_cert_reqs": None,
        },
        #"ROUTING": "ersteops.routing.channel_routing",
    },
}

# Configure Django Channels to use the parsed Redis details
# CHANNEL_LAYERS = {
#     'default': {
#         'BACKEND': 'channels_redis.core.RedisChannelLayer',
#         'CONFIG': {
#             "hosts": [{
#                 'address': f"redis://{redis_host}:{redis_port}",
#                 'password': redis_password,
#                 'ssl': url.scheme == 'rediss',  # True if scheme is 'rediss'
#                 'ssl_cert_reqs': None  # Disable SSL certificate verification
#             }],
#         },
#     },
# }


EMAIL_BACKEND = os.environ['EMAIL_BACKEND']
EMAIL_HOST = os.environ['EMAIL_HOST']
EMAIL_HOST_USER = os.environ['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD'] #past the key or password app here
EMAIL_PORT = os.environ['EMAIL_PORT']
EMAIL_USE_TLS = os.environ['EMAIL_USE_TLS']
DEFAULT_FROM_EMAIL = os.environ['DEFAULT_FROM_EMAIL']
NOTIFY_ERROR_EMAIL = os.environ['NOTIFY_ERROR_EMAIL']

MEDIA_LOCAL = ast.literal_eval(os.environ['PDF_MEDIA_LOCAL'])
# Define if media storage is local or S3
if MEDIA_LOCAL:
  MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
  MEDIA_URL = os.path.join(BASE_DIR, 'media/')
else:
  # AWS S3 Settings
  AWS_STORAGE_BUCKET_NAME = os.environ['PDF_AWS_STORAGE_BUCKET_NAME']
  AWS_ACCESS_KEY_ID = os.environ['PDF_AWS_ACCESS_KEY_ID']
  AWS_SECRET_ACCESS_KEY = os.environ['PDF_AWS_SECRET_ACCESS_KEY']
  AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
  # AWS Config
  MEDIAFILES_LOCATION = 'media'
  MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)
  #DEFAULT_FILE_STORAGE = 'ersteops.custom_storages.MediaStorage' 
  DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
  AWS_S3_FILE_OVERWRITE = False
  AWS_DEFAULT_ACL = None
