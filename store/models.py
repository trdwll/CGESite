from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    title = models.CharField(max_length=100, help_text='The title of the product that you are going to sell.')
    description = models.TextField(help_text='A description of the product.')
    price = models.FloatField(default='4.99', help_text='The price of the product.')
    is_stocked = models.BooleanField(default=True, help_text='Is the product in stock?')
    slug = models.SlugField(unique=True)

    # TODO: imagefield

    def get_absolute_url(self):
        return reverse('store_item_page', kwargs={'product_slug': self.slug})

    def __str__(self):
        return self.title


class Invoice(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
