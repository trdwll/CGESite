"""
Copyright 2019 Chain Gang Entertainment Inc. All Rights Reserved.
Original Author: Russ 'trdwll' Treadwell <russ@trdwll.com>
""" 
from django.urls import path

from . import views

urlpatterns = [
    # View
    path('', views.ForumHomeView.as_view(), name='forum_home_page'),
    path('<slug:forum_slug>/', views.ForumListView.as_view(), name='forum_list_page'),
    path('<slug:forum_slug>/<slug:topic_slug>.<int:topic_id>/', views.ForumTopicListView.as_view(), name='forum_topic_page'),

    # Create and Reply
    path('<slug:forum_slug>/create/', views.CreateTopicView.as_view(), name='forum_create_topic'),
    path('<slug:forum_slug>/<slug:topic_slug>.<int:topic_id>/reply/', views.PostReplyToTopic.as_view(), name='reply_to_topic'),

    # Pagination
    path('<slug:forum_slug>/page/<int:page>/', views.ForumListView.as_view(), name='forum_list_page_paginated'),
    path('<slug:forum_slug>/<slug:topic_slug>.<int:topic_id>/page/<int:page>/', views.ForumTopicListView.as_view(), name='forum_topic_page_paginated'),
    
    # == Moderator Settings ==
    # Topic
    path('<slug:forum_slug>/<slug:topic_slug>.<int:topic_id>/delete/', views.TrashTopicView.as_view(), name='forum_topic_page_delete'),
    path('<slug:forum_slug>/<slug:topic_slug>.<int:topic_id>/edit/', views.EditTopicView.as_view(), name='forum_topic_page_edit'),
    path('<slug:forum_slug>/<slug:topic_slug>.<int:topic_id>/lock/', views.LockTopicView.as_view(), name='forum_topic_page_lock'),
    path('<slug:forum_slug>/<slug:topic_slug>.<int:topic_id>/unlock/', views.UnlockTopicView.as_view(), name='forum_topic_page_unlock'),
    path('<slug:forum_slug>/<slug:topic_slug>.<int:topic_id>/pin/', views.PinTopicView.as_view(), name='forum_topic_page_pin'),
    path('<slug:forum_slug>/<slug:topic_slug>.<int:topic_id>/unpin/', views.UnpinTopicView.as_view(), name='forum_topic_page_unpin'),

    # Post
    path('<slug:forum_slug>/<slug:topic_slug>.<int:topic_id>/delete-post/<int:post_id>/', views.TrashPostView.as_view(), name='forum_topic_page_delete_post'),
    path('<slug:forum_slug>/<slug:topic_slug>.<int:topic_id>/edit-post/<int:post_id>/', views.EditPostView.as_view(), name='forum_topic_page_edit_post'),
]