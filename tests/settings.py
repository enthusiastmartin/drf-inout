DEBUG = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "db.sqlite3",
        "TEST": {
            "NAME": ":memory:",
        },
    },
}

INSTALLED_APPS = (
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "rest_framework",
    "tests.app",
)

SECRET_KEY = "testsecretkey"

ROOT_URLCONF = "tests.app.urls"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
