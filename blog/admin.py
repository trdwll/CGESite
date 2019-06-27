"""
Copyright 2019 Chain Gang Entertainment Inc. All Rights Reserved.
Original Author: Russ 'trdwll' Treadwell <russ@trdwll.com>
""" 

from django.contrib import admin

from .models import Category, Post, Reply

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}

class PostAdmin(admin.ModelAdmin):
    exclude = ['author']
    prepopulated_fields = {'slug': ('title', )}
    search_fields = ['title', 'category', 'tags', 'body']
    list_display = ['title', 'category', 'published_date', 'author']

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.author = request.user

        super().save_model(request, obj, form, change)

    class Media:
        js = ('ckeditor/ckeditor/ckeditor.js', 'ckeditor/ckeditor/config.js')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Reply)