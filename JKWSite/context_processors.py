"""
Copyright 2019 Film And Music Inc. All Rights Reserved.
Original Author: Russ 'trdwll' Treadwell <russ@trdwll.com>
""" 

from django.conf import settings
from .utils import get_version_checksum

def general_processors(request):
    return {
        'SITE_VERSION': get_version_checksum(),
        'GOOGLE_RECAPTCHA_PUBLIC_KEY': settings.GOOGLE_RECAPTCHA_PUBLIC_KEY,
    }