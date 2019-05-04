"""
Copyright 2019 Chain Gang Entertainment Inc. All Rights Reserved.
Original Author: Russ 'trdwll' Treadwell <russ@trdwll.com>
""" 
from django.apps import AppConfig


class StoreConfig(AppConfig):
    name = 'store'

    def ready(self):
        import .signals