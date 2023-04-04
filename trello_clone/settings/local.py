from .base import *

print("Loading local settings...")

INTERNAL_IPS = ["127.0.0.1"]

# Development apps
INSTALLED_APPS += [
    "debug_toolbar",
]

# Development middleware
MIDDLEWARE += [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]
