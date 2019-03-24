from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator

class Category(models.Model):
    title = models.CharField(max_length=100, help_text='The title of the category.')
    slug = models.SlugField(unique=True, help_text='The SEO slug for the category.')

    def get_absolute_url(self):
        return reverse('store_category_item_page', kwargs={'slug': self.slug})

    class Meta:
        db_table = 'store_category'


class StoreItem(models.Model):
    title = models.CharField(max_length=100, help_text='The title of the item.')
    description = models.CharField(max_length=100, help_text='The description of the item.')
    price = models.FloatField(default='5.00', help_text='The price of the item.')
    visible = models.BooleanField(default=True, help_text='Display this item publicly?')
    slug = models.SlugField(unique=True, help_text='The SEO slug for the item.')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, help_text='The category that this item will be listed under.')

    def get_absolute_url(self):
        return reverse('store_view_item_page', kwargs={'slug': self.slug})

    class Meta:
        db_table = 'store_item'


class Coupon(models.Model):
    code = models.CharField(max_length=20, help_text='The code that users will enter for the discount.')
    percent = models.FloatField(default='5', help_text='Percent off that will be applied from this coupon.')
    eligible_items = models.ManyToManyField(StoreItem, help_text='What items can this coupon be used on?')

    class Meta:
        db_table = 'store_coupon'


class UserRating(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(validators=[MaxValueValidator(5)])
    item = models.ForeignKey(StoreItem, on_delete=models.CASCADE)

    class Meta:
        db_table = 'store_item_rating'


class UserReview(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(StoreItem, on_delete=models.CASCADE)
    review = models.TextField()

    class Meta:
        db_table = 'store_item_review'


# Invoice