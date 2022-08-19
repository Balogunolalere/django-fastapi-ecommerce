from django.contrib.admin import ModelAdmin, register
# Register your models here.

from .models import Product, Review, Order, OrderItem, Shipping

@register(Product)
class ProductAdmin(ModelAdmin):
    list_display = ['name', 'description', 'price', 'category','stock', 'image']
    list_filter = ['name', 'description', 'price', 'category', 'stock', 'image']
    search_fields = ['name', 'description', 'price', 'category', 'stock', 'image']
    list_per_page = 25
    icon_name = 'local_drink'


@register(Review)
class ReviewAdmin(ModelAdmin):
    list_display = ['product', 'user', 'rating', 'review']
    list_filter = ['product', 'user', 'rating', 'review']
    search_fields = ['product', 'user', 'rating', 'review']
    list_per_page = 25
    icon_name = 'stars'


@register(Order)
class OrderAdmin(ModelAdmin):
    list_display = ['user', 'product', 'tax', 'order_shipping', 'total', 'is_paid', 'is_delivered', 'delivered_at', 'quantity', 'created_at', 'payment_method']
    list_filter = ['user', 'product', 'tax', 'order_shipping', 'total', 'is_paid', 'is_delivered', 'delivered_at', 'quantity', 'created_at', 'payment_method']
    search_fields = ['user', 'product', 'tax', 'order_shipping', 'total', 'is_paid', 'is_delivered', 'delivered_at', 'quantity', 'created_at', 'payment_method']
    list_per_page = 25
    icon_name = 'shopping_basket'

@register(OrderItem)
class OrderItemAdmin(ModelAdmin):
    list_display = ['order', 'product', 'quantity']
    list_filter = ['order', 'product', 'quantity']
    search_fields = ['order', 'product', 'quantity']
    list_per_page = 25
    icon_name = 'shopping_cart'

@register(Shipping)
class ShippingAdmin(ModelAdmin):
    list_display = ['shipping_order', 'name', 'address', 'city', 'state', 'zipcode', 'country', 'phone']
    list_filter = ['shipping_order', 'name', 'address', 'city', 'state', 'zipcode', 'country', 'phone']
    search_fields = ['shipping_order', 'name', 'address', 'city', 'state', 'zipcode', 'country', 'phone']
    list_per_page = 25
    icon_name = 'local_shipping'