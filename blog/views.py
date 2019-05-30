"""
Copyright 2019 Chain Gang Entertainment Inc. All Rights Reserved.
Original Author: Russ 'trdwll' Treadwell <russ@trdwll.com>
""" 

from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.generic import View, ListView
from django.db.models import Count, Max

from .models import Category, Post

import random

def get_random_post():
    """
    Credits: http://books.agiliq.com/projects/django-orm-cookbook/en/latest/random.html
    
    Get random object from the database.
    """
    max_id = Post.objects.all().aggregate(max_id=Max('id'))['max_id']
    while True:
        pk = random.randint(1, max_id)
        post = Post.objects.filter(pk=pk).first()
        if post:
            return post


class BlogHomeView(ListView):
    """
    Blog home view for displaying blog posts on the blog home page.
    We use a ListView so we can do pagination easier and since we're needing a list rather than one object.
    """
    model = Post
    template_name = 'blog/blog-home-page.html'
    paginate_by = 8
    context_object_name = 'posts'

    def get_queryset(self, *args, **kwargs):
        # We override get_queryset so we can only get published Posts and list them by newest
        return get_list_or_404(Post.objects.order_by('-published_date'), is_published=True)

    def get_context_data(self, **kwargs):
        # We override get_context_data so we can pass some extra data to the home page
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all().order_by('title')[:8]
        context['random_post'] = get_random_post()
        return context


class BlogPostView(View):
    """
    Blog post view for displaying the specified blog post.
    """
    template_name = 'blog/blog-post-page.html'

    def get(self, request, slug):
        # We get the blog post object from the slug that's passed into the query
        post = get_object_or_404(Post.objects.filter(slug=slug, is_published=True))
        return render(request, self.template_name, {'post': post})


class BlogCategoryView(ListView):
    """
    Blog category view for displaying blog posts that has the same category.
    We use a ListView so we can do pagination easier and since we're needing a list rather than one object.
    """
    model = Post
    template_name = 'blog/blog-category-page.html'
    paginate_by = 12
    context_object_name = 'posts'

    def get_queryset(self, *args, **kwargs):
        # We override get_queryset so we can only get published Posts, get the posts that have the same category, and list them by newest
        return get_list_or_404(Post.objects.filter(
            is_published=True, 
            category=Category.objects.filter(slug=self.kwargs['slug']).first()
        ).order_by('-published_date'))



class BlogPostReactView(View):
    def post(self, request, slug, react):
        post = get_object_or_404(Post.objects.filter(slug=slug))

        if react == '1' or react == '0':
            pass

        return redirect('blog_post_page', slug=slug)


        # TODO: check if the user has already reacted and if they have then remove it, but don't allow the user to vote like and dislike

