"""
Copyright 2019 Film And Music Inc. All Rights Reserved.
Original Author: Russ 'trdwll' Treadwell <russ@trdwll.com>
""" 

from django.urls import path

from . import views


urlpatterns = [
    path('', views.StoreHomeView.as_view(), name='store_home_page'),
    path('item/<slug:slug>/', views.StoreItemView.as_view(), name='store_view_item_page'),
    path('category/<slug:slug>/', views.StoreItemCategoryView.as_view(), name='store_category_item_page'),
]
