from djantic import ModelSchema

from store.models import Product


class ProductSchema(ModelSchema):
    class Config:
        model = Product
        include = ['name', 'description', 'price', 'category', 'stock', 'image', 'created_at']