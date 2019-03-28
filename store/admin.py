"""
Copyright 2019 Film And Music Inc. All Rights Reserved.
Original Author: Russ 'trdwll' Treadwell <russ@trdwll.com>
""" 

from django.contrib import admin

from .models import (
    StoreItem, 
    Category, 
    Coupon, 
    UserCart
)


class StoreAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}


admin.site.register(Category, StoreAdmin)
admin.site.register(StoreItem, StoreAdmin)
admin.site.register(Coupon)
admin.site.register(UserCart)