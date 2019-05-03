from django.contrib import admin

from .models import Product, Coupon


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