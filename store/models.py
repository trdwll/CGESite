"""
Copyright 2019 Film And Music Inc. All Rights Reserved.
Original Author: Russ 'trdwll' Treadwell <russ@trdwll.com>
""" 

from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator



def store_upload_path(instance, filename):
    return 'store/%s/%s' % (instance.slug, filename)


class Category(models.Model):
    title = models.CharField(max_length=100, help_text='The title of the category.')
    slug = models.SlugField(unique=True, help_text='The SEO slug for the category.')

    def get_absolute_url(self):
        return reverse('store_category_item_page', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'store_category'


class StoreItem(models.Model):
    title = models.CharField(max_length=100, help_text='The title of the item.')
    description = models.CharField(max_length=150, help_text='The description of the item.')
    price = models.FloatField(default='5.00', help_text='The price of the item.')
    slug = models.SlugField(unique=True, help_text='The SEO slug for the item.')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, help_text='The category that this item will be listed under.')
    image = models.ImageField(verbose_name='Store Image', upload_to=store_upload_path, help_text='The image that will be displayed for the item on the store page.')

    is_visible = models.BooleanField(verbose_name='Visible?', default=True, help_text='Display this item publicly?')
    is_stocked = models.BooleanField(verbose_name='Stocked?', default=True, help_text='Is this item in stock?')
    is_free_shipping = models.BooleanField(verbose_name='Free Shipping?', default=True, help_text='Does this item have free shipping?')

    def get_absolute_url(self):
        return reverse('store_view_item_page', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'store_item'


class Coupon(models.Model):
    code = models.CharField(max_length=20, help_text='The code that users will enter for the discount.')
    percent = models.FloatField(default='5', help_text='Percent off that will be applied from this coupon.')
    eligible_items = models.ManyToManyField(StoreItem, help_text='What items can this coupon be used on?')

    class Meta:
        db_table = 'store_coupon'


# Invoice



class UserCart(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    # only allowing a m2m field it makes it where the user can only purchase 1 of an item at a time for example product A and B, not 2 of product A
    items = models.ManyToManyField(StoreItem, help_text='The items that are in this users cart.') 
    coupon = models.CharField(max_length=20, blank=True)
    total_price = models.FloatField()

    def __str__(self):
        return self.owner.username + '\'s cart'

    class Meta:
        db_table = 'store_cart'


# Wishlist