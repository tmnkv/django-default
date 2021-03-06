import os
import sys

from unipath import Path
{% if cookiecutter.use_dotenv == 'y' -%}
from dotenv import load_dotenv
{%- endif %}

from config.settings.celery import *
{% if cookiecutter.use_jet_admin == 'y' -%}
from config.settings.jet import *
{%- endif %}


BASE_DIR = Path(__file__).ancestor(3)

APPS_DIR = BASE_DIR.child('apps')
sys.path.append(APPS_DIR)

{% if cookiecutter.use_dotenv == 'y' -%}
DOTENV_PATH = BASE_DIR.child('.env')

load_dotenv(DOTENV_PATH)

{%- endif %}
SECRET_KEY = os.environ['SECRET_KEY']

{% if cookiecutter.use_mptt == 'y' -%}
SITE_ID = 1
{%- endif %}

INSTALLED_APPS = [
    {% if cookiecutter.use_jet_admin == 'y' -%}
    'jet.dashboard',
    'jet',
    {%- endif %}
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    {% if cookiecutter.use_mptt == 'y' -%}
    'django.contrib.sites',
    {%- endif %}
    'imagekit',
    'django_extensions',
    {% if cookiecutter.use_rest_framework == 'y' -%}
    'rest_framework',
    {%- endif %}
    {% if cookiecutter.use_adminsortable == 'y' -%}
    'adminsortable2',
    {%- endif %}
    'apps.core.apps.CoreConfig',
]

MIDDLEWARE_CLASSES = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
]

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

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR.child('templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                {% if cookiecutter.use_mptt == 'y' -%}
                'apps.core.context_processors.add_page',
                'apps.core.context_processors.add_header',
                'apps.core.context_processors.add_footer',
                {%- endif %}
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True
USE_L10N = True
USE_TZ = True

# static
STATICFILES_DIRS = [BASE_DIR.child("static").child("build")]
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR.child("collect_static")

# media
MEDIA_ROOT = BASE_DIR.child("media")
MEDIA_URL = '/media/'
