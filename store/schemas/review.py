from djantic import ModelSchema
from store.models import Review
from store.schemas.product import ProductSchema




class ReviewSchema(ModelSchema):
    product : ProductSchema
    class Config:
        model = Review
        include = ['product', 'user', 'rating', 'review', 'created_at']