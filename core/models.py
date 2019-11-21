from django.conf import settings
from django.db import models
from django.shortcuts import reverse
from django import forms
from django.contrib.auth.models import User


CATEGORY_CHOICES = (
    ('Fruits', 'Fruits'),
    ('Vegetables', 'Vegetables'),
    ('Dairy Products', 'Dairy Products'),
    ('Eggs and Meats', 'Eggs and Meats')
)

class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField() 
    discount_price = models.FloatField(blank=True, null=True)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=20)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    # image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('core:product', kwargs={
            'slug':self.slug
        })

    def get_add_to_cart_url(self):
        return reverse('core:add-to-cart', kwargs={
            'slug':self.slug
        })

    def get_remove_from_cart_url(self):
        return reverse('core:remove-from-cart', kwargs={
            'slug':self.slug
        })


class CheckOut(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    address = models.CharField( max_length=100)
    phonenumber = models.CharField(max_length=100)
    paymentoption = models.CharField(max_length=100)
    deliveryoption = models.CharField(max_length=100)
    
    def __str__(self):
        return self.user.username

from django.utils import timezone
today = timezone.now

class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
    item = models.ForeignKey(Item, on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.FloatField(default=1)
    ordered = models.BooleanField(default=False)
    delievered = models.BooleanField(default=False)
    deliveryoption = models.CharField(max_length=100)
    ordered_date = models.DateField(default=today)
    # total = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.quantity} of {self.item.title}"

    def get_total_item_price(self):
        return self.quantity * self.item.price 
    
    def get_total_discount_item_price(self):
        return self.quantity * self.item.discount_price

    def get_amount_saved(self):
        return self.get_total_item_price() - self.get_total_discount_item_price()

    def get_final_price(self):
        if self.item.discount_price:
            return self.get_total_discount_item_price()
        return self.get_total_item_price()


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateField()
    ordered = models.BooleanField(default=False)
    billing_address = models.ForeignKey('Checkout', on_delete=models.SET_NULL, blank=True, null=True)
    # total_price = models.IntegerField(blank=True)
    
    def __str__(self):
        return self.user.username

    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()
        return total 

