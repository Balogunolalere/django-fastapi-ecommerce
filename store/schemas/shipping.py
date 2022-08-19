from djantic import ModelSchema
from store.models import Shipping
from store.schemas.order import OrderSchema



class ShippingSchema(ModelSchema):
    order : OrderSchema
    class Config:
        model = Shipping
        include = ['order', 'address', 'city', 'zipcode', 'country', 'name', 'phone', 'state']
