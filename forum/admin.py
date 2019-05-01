from django.contrib import admin
from .models import Forum, Topic, Post

class ForumAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}

class TopicAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}

admin.site.register(Forum, ForumAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Post)
