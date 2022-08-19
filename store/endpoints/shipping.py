from fastapi import APIRouter
from store.models import Shipping
from store.schemas.shipping import ShippingSchema
from typing import List 

router = APIRouter()


@router.get("/shipping", response_model=List[ShippingSchema], status_code=200)
def get_shippings():
    shippings = Shipping.objects.all()
    return [ShippingSchema.from_django(shipping) for shipping in shippings]


# @router.post("/shipping", response_model=ShippingSchema, status_code=201)
# def create_shipping(order: int, address: str, city: str, zipcode: str, country: str, name: str, phone: str, state: str):
#     shipping = Shipping.objects.create()
#     shipping.order = order
#     shipping.address = address
#     shipping.city = city
#     shipping.zipcode = zipcode
#     shipping.country = country
#     shipping.name = name
#     shipping.phone = phone
#     shipping.state = state
#     shipping.save()
#     return shipping


# @router.put("/shipping/{id}", response_model=ShippingSchema, status_code=200)
# def update_shipping(id: int, order: int, address: str, city: str, zipcode: str, country: str, name: str, phone: str, state: str):
#     shipping = Shipping.objects.get(id=id)
#     shipping.order = order
#     shipping.address = address
#     shipping.city = city
#     shipping.zipcode = zipcode
#     shipping.country = country
#     shipping.name = name
#     shipping.phone = phone
#     shipping.state = state
#     shipping.save()
#     return shipping


# @router.delete("/shipping/{id}", status_code=204)
# def delete_shipping(id: int):
#     shipping = Shipping.objects.get(id=id)
#     shipping.delete()
#     return None

