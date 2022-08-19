from djantic import ModelSchema
from store.models import OrderItem
from store.schemas.product import ProductSchema
from store.schemas.order import OrderSchema


class OrderItemSchema(ModelSchema):
    product : ProductSchema
    order : OrderSchema
    class Config:
        model = OrderItem
        include = ['user', 'product','order' ,'quantity']


