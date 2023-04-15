from pathlib import Path

from google.cloud import secretmanager

client = secretmanager.SecretManagerServiceClient()

# Location of the secrets

parent = "projects/sonorous-lyceum-382300/secrets"

# The version of the secrets

version = "latest"

# Keys in this dict should be the same as on Google Cloud
# as they will be used to retrieve their values from there.

secrets = {
    "SECRET_KEY": "",
    "DEBUG": "",
    "DB_NAME": "",
    "DB_USER": "",
    "DB_PASS": "",
    "DB_HOST": "",
    "DB_PORT": "",
}

# Setting the secrets in the secrets dictionary by getting them from Google Clouds.

for secret in secrets:
    secrets[secret] = client.access_secret_version(
        request={"name": f"{parent}/{secret}/versions/{version}"}
    ).payload.data.decode()  # Decoding because the value comes in as a bytestring.

DEBUG = bool(secrets["DEBUG"])

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = secrets["SECRET_KEY"]

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_version_checks",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# Database settings
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": secrets["DB_NAME"],
        "USER": secrets["DB_USER"],
        "PASSWORD": secrets["DB_PASS"],
        "HOST": secrets["DB_HOST"],
        "PORT": secrets["DB_PORT"],
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation"
        ".UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

ROOT_URLCONF = "trello_clone.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "static/"

USE_TZ = True

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

VERSION_CHECKS = {"python": "==3.11.*", "postgresql": "==14.*"}
