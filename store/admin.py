from django.contrib import admin

from .models import Category, StoreItem, Coupon, UserRating


class StoreAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}

admin.site.register(Category, StoreAdmin)
admin.site.register(StoreItem, StoreAdmin)
admin.site.register(Coupon)
admin.site.register(UserRating)