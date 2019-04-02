"""
Copyright 2019 Film And Music Inc. All Rights Reserved.
Original Author: Russ 'trdwll' Treadwell <russ@trdwll.com>
""" 

from django.urls import path

from .views import BlogHomeView, BlogPostView, BlogCategoryView

urlpatterns = [
    path('', BlogHomeView.as_view(), name='blog_home_page'),
    path('page/<int:page>/', BlogHomeView.as_view(), name='blog_home_page_paginated'),

    path('post/<slug:slug>/', BlogPostView.as_view(), name='blog_post_page'),

    path('category/<slug:slug>/', BlogCategoryView.as_view(), name='blog_category_page'),
    path('category/<slug:slug>/page/<int:page>/', BlogCategoryView.as_view(), name='blog_category_page_paginated'),
]