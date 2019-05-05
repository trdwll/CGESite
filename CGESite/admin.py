"""
Copyright 2019 Chain Gang Entertainment Inc. All Rights Reserved.
Original Author: Russ 'trdwll' Treadwell <russ@trdwll.com>
""" 

from django.contrib import admin

from .models import HomeData, HomeCarousel, Character

class HomeCarouselAdmin(admin.TabularInline):
    model = HomeCarousel
    extra = 2

class SiteAdmin(admin.ModelAdmin):
    #inlines = [HomeCarouselAdmin, ]
    
    def has_add_permission(self, *args, **kwargs):
        # restrict only 1 entry of this model
        return not HomeData.objects.exists()

admin.site.register(HomeData, SiteAdmin)

admin.site.register(HomeCarousel)
admin.site.register(Character)
