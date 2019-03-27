from django.contrib import admin

from .models import HomeData



class SiteAdmin(admin.ModelAdmin):
    
    # restrict only 1 entry of this model
    def has_add_permission(self, *args, **kwargs):
        return not HomeData.objects.exists()

admin.site.register(HomeData, SiteAdmin)
