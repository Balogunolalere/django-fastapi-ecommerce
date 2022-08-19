from djantic import ModelSchema

from store.models import Order
from store.schemas.product import ProductSchema

class OrderSchema(ModelSchema):
    product : ProductSchema
    class Config:
        model = Order
        include = ['user', 'product', 'quantity', 'created_at', 'order_shipping', 'quantity', 'total', 'tax', 'delivered_at', 'is_paid', 'is_delivered', 'payment_method']