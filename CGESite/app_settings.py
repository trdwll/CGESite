"""
Copyright 2019 Chain Gang Entertainment Inc. All Rights Reserved.
Original Author: Russ 'trdwll' Treadwell <russ@trdwll.com>
""" 

FORUM_TOPIC_LIST_PAGINATION = 20
FORUM_LIST_PAGINATION = 20
STORE_LIST_PAGINATION = 24


NEWSLETTER_UNSUBSCRIBE_LINK = 'https://chaingangentertainment.com/newsletter/unsubscribe/'

SITE_TITLE = 'Chain Gang Entertainment'
NO_REPLY_EMAIL = 'no-reply@chaingangentertainment.com'
CONTACT_EMAIL = 'contact@chaingangentertainment.com'


PAYPAL_RECEIVER_EMAIL = 'paypal@trdwll.com'


HTML_MINIFY = False
EXCLUDE_FROM_MINIFYING = ('dev/')

OTP_TOTP_ISSUER = 'Chain Gang Entertainment Inc'

GOOGLE_RECAPTCHA_SECRET_KEY = '6LcRWKIUAAAAAA7y7Q0BnX7QDLTSB-9zTRifpnOz' 
GOOGLE_RECAPTCHA_PUBLIC_KEY = '6LcRWKIUAAAAAJPHz1o432RJbwcm3nwdNP-MHXca'


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
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '704441209375-fu1nen7t2ka9viq37vkv5vgdgho5ld9p.apps.googleusercontent.com'  
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'dfxprhPETWlBunJ0606nFMNg'

SOCIAL_AUTH_TWITTER_KEY = ''
SOCIAL_AUTH_TWITTER_SECRET = ''

SOCIAL_AUTH_TWITCH_KEY = '39ojiu3xa9h04vicw687gsl2ibjpfo'
SOCIAL_AUTH_TWITCH_SECRET = 'o4vyy7cr36yfbx3uoltvpgda8002oy'

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
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
)

#SOCIAL_AUTH_REDIRECT_IS_HTTPS = True


LANGUAGE_CODE = 'en'

CART_SESSION_ID = 'cart'
