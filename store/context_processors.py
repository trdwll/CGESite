"""
Copyright 2019 Chain Gang Entertainment Inc. All Rights Reserved.
Original Author: Russ 'trdwll' Treadwell <russ@trdwll.com>
""" 
from .cart import Cart

def general_processors(request):
    return {
        'cart': Cart(request) 
    }
