"""
Copyright 2019 Film And Music Inc. All Rights Reserved.
Original Author: Russ 'trdwll' Treadwell <russ@trdwll.com>
""" 

import os
from .app_settings import *

from django.contrib.messages import constants as message_constants


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'r4y-g_+yy#w+^yl0b(pc9gpw92!y&fc)=x^b-m-6txd5i9v!-f'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'fam.dev.trdwll.com', '10.5.1.104']


# Application definition

INSTALLED_APPS = [
    # Django default apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Our apps
    'JKWSite',
    'blog',
    'users',
    'forum',
    'store',

    # 3rd party apps
    'django_otp',
    'django_otp.plugins.otp_totp',
    'social_django',
    'taggit',
    'paypal.standard.ipn',
    'localflavor',
]


MIDDLEWARE = [
    # Django middleware
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # htmlminify middleware
    'htmlmin.middleware.HtmlMinifyMiddleware',
    'htmlmin.middleware.MarkRequestMiddleware',

    # OTP middleware
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django_otp.middleware.OTPMiddleware',
]

ROOT_URLCONF = 'JKWSite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.template.context_processors.request',
                'django.contrib.messages.context_processors.messages',

                'JKWSite.context_processors.general_processors',
                'store.context_processors.general_processors',

                'social_django.context_processors.backends', # Django Social Auth
                'social_django.context_processors.login_redirect', # Django Social Auth
            ],
        },
    },
]

WSGI_APPLICATION = 'JKWSite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
    # 'default': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': 'fam',
    #     'USER': 'famuser',
    #     'PASSWORD': '',
    #     'HOST': 'server.dev.trdwll.com',
    #     #'HOST': 'inline',
    #     'PORT': '3306',
    # }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    },
}

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
    },
}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    { 'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]


PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.Argon2PasswordHasher',
]

MESSAGE_TAGS = {
    message_constants.DEBUG: 'alert-danger',
    message_constants.INFO: 'alert-info',
    message_constants.SUCCESS: 'alert-success',
    message_constants.WARNING: 'alert-warning',
    message_constants.ERROR: 'alert-danger'
}


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'America/New_York'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
  #  '/var/www/mydomain.com/public_html/static/',
]
# STATIC_ROOT = os.path.join(BASE_DIR, "static")


# MEDIA_ROOT = '/var/www/mydomain.com/public_html/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = '/media/'

FILE_UPLOAD_PERMISSIONS = 0o644

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
LOGIN_URL = '/auth/login/'
CSRF_COOKIE_NAME = 'jkhasjdhjaksdh'


if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    PAYPAL_TEST = True
else:
    EMAIL_USE_TLS = True
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_PORT = 587
    EMAIL_HOST_USER = 'me@gmail.com'
    EMAIL_HOST_PASSWORD = 'password'
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

    PAYPAL_TEST = False

PAYPAL_RECEIVER_EMAIL = 'paypal@trdwll.com'