"""
Copyright 2019 Film And Music Inc. All Rights Reserved.
Original Author: Russ 'trdwll' Treadwell <russ@trdwll.com>
""" 

from .models import UserCart

from django.contrib.auth.models import User

def store_processors(request):
    return {
        'cart': UserCart.objects.filter(owner=User.objects.filter(username=request.user.username).first()).first()
    }