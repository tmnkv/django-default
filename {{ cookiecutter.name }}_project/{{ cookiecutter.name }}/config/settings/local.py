from config.settings.base import *


DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR.child('db.sqlite3'),
    }
}
{% if cookiecutter.use_debug_toolbar == 'y' -%}
MIDDLEWARE_CLASSES += ['debug_toolbar.middleware.DebugToolbarMiddleware',]

INSTALLED_APPS = INSTALLED_APPS + [
    'debug_toolbar',
]

INTERNAL_IPS = '127.0.0.1'
{%- endif %}

ROOT_URLCONF = 'config.urls.local'



SESSION_ENGINE = 'django.contrib.sessions.backends.db'
