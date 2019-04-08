"""
Copyright 2019 Film And Music Inc. All Rights Reserved.
Original Author: Russ 'trdwll' Treadwell <russ@trdwll.com>
""" 

import os

from django.contrib.messages import constants as message_constants

from machina import get_apps as get_machina_apps
from machina import MACHINA_MAIN_STATIC_DIR

from oscar.defaults import *
from oscar import OSCAR_MAIN_TEMPLATE_DIR
from oscar import get_core_apps

from django.utils.translation import ugettext_lazy as _

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
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.flatpages',

    # Our apps
    'JKWSite',
    'blog',
    'users',

    # 3rd party apps
    'django_otp',
    'django_otp.plugins.otp_totp',
    'social_django',
    'taggit',

    'paypal',

    # Machina related apps:
    'mptt',
    # 'haystack', # dep of oscar so get_core_apps includes it
    'widget_tweaks',
] + get_machina_apps() + get_core_apps()

SITE_ID = 1

OSCAR_DASHBOARD_NAVIGATION.append(
{
    'label': _('PayPal'),
    'icon': 'icon-globe',
    'children': [
        {
            'label': _('Express transactions'),
            'url_name': 'paypal-express-list',
        },
    ]
})


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

    'machina.apps.forum_permission.middleware.ForumPermissionMiddleware',

    'oscar.apps.basket.middleware.BasketMiddleware',
]

ROOT_URLCONF = 'JKWSite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            os.path.join(BASE_DIR, 'templates/machina'), # custom design for machina
            OSCAR_MAIN_TEMPLATE_DIR
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

                'machina.core.context_processors.metadata',

                'oscar.apps.search.context_processors.search_form',
                'oscar.apps.promotions.context_processors.promotions',
                'oscar.apps.checkout.context_processors.checkout',
                'oscar.apps.customer.notifications.context_processors.notifications',
                'oscar.core.context_processors.metadata',

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
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'fam',
        'USER': 'famuser',
        'PASSWORD': '',
        'HOST': 'server.dev.trdwll.com',
        #'HOST': 'inline',
        'PORT': '3306',
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    },
    'machina_attachments': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/tmp',
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
    MACHINA_MAIN_STATIC_DIR # might not need this....
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

SITE_TITLE = 'Film And Music'
NO_REPLY_EMAIL = 'no-reply@mydomain.com'

HTML_MINIFY = True

OTP_TOTP_ISSUER = 'Film And Music Inc'

# Machina Settings (forum module)
MACHINA_FORUM_NAME = 'FreeDome'
MACHINA_FORUM_IMAGE_UPLOAD_TO = 'forum/forum_images'
MACHINA_ATTACHMENT_FILE_UPLOAD_TO = 'forum/attachments'
MACHINA_PROFILE_AVATAR_UPLOAD_TO = 'forum/avatars'
MACHINA_TOPIC_ANSWER_SUBJECT_PREFIX = ''
MACHINA_TOPIC_POSTS_NUMBER_PER_PAGE = 20
MACHINA_BASE_TEMPLATE_NAME = 'machina/_base.html'


GOOGLE_RECAPTCHA_SECRET_KEY = '6LcDeJoUAAAAAF7ASXpcAoY9SpGxRKLhKVlBUtQ5'
GOOGLE_RECAPTCHA_PUBLIC_KEY = '6LcDeJoUAAAAAKOl-0zhUa1m0fZK51Eby_ZzhP0k'


AUTHENTICATION_BACKENDS = (
    'social_core.backends.open_id.OpenIdAuth',  # for Google authentication
    'social_core.backends.google.GoogleOpenId',  # for Google authentication
    'social_core.backends.google.GoogleOAuth2',  # for Google authentication
    'social_core.backends.github.GithubOAuth2',  # for Github authentication
    'social_core.backends.twitter.TwitterOAuth', # for Twitter authentication
    'social_core.backends.twitch.TwitchOAuth2', # for Twitch authentication
    'social_core.backends.discord.DiscordOAuth2', # for Discord authentication

    'users.backends.CaseInsensitiveModelBackend',
    'django.contrib.auth.backends.ModelBackend', # Default Django authentication (username/password)
)


# Social Auth Settings
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '536162012155-fcmmannh5i8rr7tup3qfqpcgtatohtt8.apps.googleusercontent.com'  
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'EJXU6nKBiOGCfcMfcjUVSb18'

SOCIAL_AUTH_TWITTER_KEY = ''
SOCIAL_AUTH_TWITTER_SECRET = ''

SOCIAL_AUTH_TWITCH_KEY = '3lgibxzrdxfv4mgvvsg28m9pnzl5ln'
SOCIAL_AUTH_TWITCH_SECRET = '0ogvrk6jakeiqrm0i3qelxt6apy20'

SOCIAL_AUTH_DISCORD_KEY = '560580803633872896'  
SOCIAL_AUTH_DISCORD_SECRET = 'EDaRhRENNkvEaJ-mUzPZAK0H13DEER5q'

SOCIAL_AUTH_DISCORD_IGNORE_DEFAULT_SCOPE = True
SOCIAL_AUTH_DISCORD_SCOPE = [
    'identify', 'email'
]

SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.auth_allowed',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.user.create_user',
    #'members.models.save_profile', 
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
)

#SOCIAL_AUTH_REDIRECT_IS_HTTPS = True

PAYPAL_API_USERNAME = 'russ+fam_api1.trdwll.com'
PAYPAL_API_PASSWORD = '7DKGX7VZPVE66YWH'
PAYPAL_API_SIGNATURE = 'AM.mJXg9D4CJVmLuVr1CY6gzeeHIAKpJOOCzPsP2rLQK5vcqiM5B1hPY'

OSCAR_SHOP_NAME = 'FAM Store'
#OSCAR_SHOP_TAGLINE = 'Demo'

LANGUAGE_CODE = 'en'