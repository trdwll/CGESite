from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _


class Product(models.Model):
    title = models.CharField(max_length=100, help_text='The title of the product that you are going to sell.')
    description = models.TextField(help_text='A description of the product.')
    price = models.DecimalField(max_digits=10, decimal_places=2, default='4.99')
    is_stocked = models.BooleanField(default=True, help_text='Is the product in stock?')
    stock = models.PositiveIntegerField()
    image = models.ImageField(upload_to='store/products/%Y/%m/%d', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True)

    def get_absolute_url(self):
        return reverse('store_item_page', kwargs={'product_id': self.id, 'product_slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-created',)


class Coupon(models.Model):
    code = models.CharField(max_length=50, unique=True)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    discount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    is_active = models.BooleanField()

    def __str__(self):
        return self.code


class Order(models.Model):
    first_name = models.CharField(_('first name'), max_length=50)
    last_name = models.CharField(_('last name'), max_length=50)
    email = models.EmailField(_('e-mail'))
    address = models.CharField(_('address'), max_length=250)
    postal_code = models.CharField(_('postal code'),  max_length=20)
    city = models.CharField(_('city'), max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    coupon = models.ForeignKey(Coupon, related_name='orders', null=True, blank=True, on_delete=models.CASCADE)
    discount = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        total_cost = sum(item.get_cost() for item in self.items.all())
        return total_cost - total_cost * (self.discount / Decimal('100'))


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity