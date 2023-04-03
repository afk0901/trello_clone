from .base import *

print("Loading local settings...")

DEBUG = True

INTERNAL_IPS = ["127.0.0.1"]

# Development apps
INSTALLED_APPS += [
    "debug_toolbar",
]

# Database settings
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "trello_clone",
        "USER": "postgres",
        "PASSWORD": "12345",
        "HOST": "localhost",
        "PORT": "5432",
    }
}

# Development middleware
MIDDLEWARE += [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]
