from django.contrib import admin

from .models import HomeData



class SiteAdmin(admin.ModelAdmin):
    
    # restrict only 1 entry of this model
    def has_add_permission(self, *args, **kwargs):
        return not HomeData.objects.exists()

admin.site.register(HomeData, SiteAdmin)



# Forum/Spirit specific admin

from spirit.category.models import Category
from spirit.comment.models import Comment
from spirit.topic.models import Topic
from spirit.user.models import UserProfile

admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Topic)
admin.site.register(UserProfile)
