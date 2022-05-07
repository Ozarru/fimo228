from django.db import models
from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(
        User, null=True, on_delete=models.CASCADE, blank=True)
    name = models.CharField(max_length=256)
    email = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Couture(models.Model):
    name = models.CharField(max_length=6)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128)
    couture = models.ForeignKey(Couture, on_delete=models.SET_NULL, null=True)
    price = models.FloatField(default=0.0)
    quantity = models.IntegerField(default=0)
    collection = models.CharField(max_length=128, blank=True)
    description = models.TextField(blank=True)
    thumbnail = models.ImageField(upload_to='products', blank=True, null=True)
    date_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product', kwargs={'slug': self.slug})


class Order(models.Model):
    order_id = models.CharField(max_length=24)
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, null=True)
    odered_at = models.DateTimeField(auto_now_add=True)
    is_payed = models.BooleanField(default=False, null=False, blank=False)
    is_delivered = models.BooleanField(default=False, null=False, blank=False)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

    def __str__(self):
        return str(self.id)


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total

    def __str__(self):
        return str(self.id)


class ShippingInfo(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    phone = models.CharField(max_length=32, blank=False, null=False)
    address = models.CharField(max_length=256, blank=False, null=False)
    city = models.CharField(max_length=64, blank=False, null=False)
    country = models.CharField(max_length=64, blank=False, null=False)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
