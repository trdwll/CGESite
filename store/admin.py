"""
Copyright 2019 Chain Gang Entertainment Inc. All Rights Reserved.
Original Author: Russ 'trdwll' Treadwell <russ@trdwll.com>
""" 
from django.contrib import admin

from .models import Product, Coupon, Order, OrderItem


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}
    list_display = ['title', 'slug', 'price', 'stock', 'created', 'updated']
    list_filter = ['created', 'updated']
    list_editable = ['price', 'stock']


class CouponAdmin(admin.ModelAdmin):
    list_display = ['code', 'valid_from', 'valid_to', 'discount']
    list_filter = ['valid_from', 'valid_to']
    search_fields = ['code']


admin.site.register(Product, ProductAdmin)
admin.site.register(Coupon, CouponAdmin)
admin.site.register(Order)
admin.site.register(OrderItem)