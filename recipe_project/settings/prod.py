from .base import *
import os
import dj_database_url

SECRET_KEY = os.environ.get("SECRET_KEY_ENV")

DATABASES = {
	"default": dj_database_url.parse(os.environ.get("DATABASE_URL"))
}

DEBUG = False

ALLOWED_HOSTS = []

SESSION_COOKIE_SECURE = True

CSRF_COOKIE_SECURE = True

SECURE_SSL_REDIRECT = True

SECURE_HSTS_SECONDS = 60

SECURE_HSTS_INCLUDE_SUBDOMAINS = True

SECURE_HSTS_PRELOAD = True