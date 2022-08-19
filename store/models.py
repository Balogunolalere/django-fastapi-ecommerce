from django.db import models
from django.contrib.auth.models import User
# Create your models here.






class Product(models.Model):

    class Categories(models.TextChoices):
    
        HAIR = 'HAIR'
        SKIN = 'SKIN CARE'
        MAKEUP = 'MAKEUP'
        PERFUME = 'PERFUME'
        SOAP = 'SOAP'
        HAIR_PRODUCT = 'HAIR PRODUCT'


    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    category = models.CharField(max_length=20,choices=Categories.choices, default=Categories.HAIR)
    stock = models.IntegerField(blank=True, null=True, default=0)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.AutoField(primary_key=True, editable=False)


    def __str__(self):
        return self.name


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)        
    rating = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    review = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return self.review


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    tax = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    order_shipping = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    is_paid = models.BooleanField(default=False)
    payment_method = models.CharField(max_length=255, blank=True, null=True)
    is_delivered = models.BooleanField(default=False)
    delivered_at = models.DateTimeField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return self.product.name


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(blank=True, null=True, default=0)
    id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return self.product.name

class Shipping(models.Model):
    shipping_order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True,)
    name = models.CharField(max_length=255, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    zipcode = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return self.name