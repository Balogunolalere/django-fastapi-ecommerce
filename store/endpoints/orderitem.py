from fastapi import APIRouter
from store.models import OrderItem

from store.schemas.orderitem import OrderItemSchema
from typing import List

router = APIRouter()


@router.get("/orderitem", response_model=List[OrderItemSchema], status_code=200)
def get_orderitems():
    orderitems = OrderItem.objects.all()
    return [OrderItemSchema.from_django(orderitem) for orderitem in orderitems]


# @router.post("/orderitem", response_model=OrderItemSchema, status_code=201)
# def create_orderitem(user: int, product: int, order: int, quantity: int):
#     orderitem = OrderItem.objects.create()
#     orderitem.user = user
#     orderitem.product = product
#     orderitem.order = order
#     orderitem.quantity = quantity
#     orderitem.save()
#     return orderitem


# @router.put("/orderitem/{id}", response_model=OrderItemSchema, status_code=200)
# def update_orderitem(id: int, user: int, product: int, order: int, quantity: int):
#     orderitem = OrderItem.objects.get(id=id)
#     orderitem.user = user
#     orderitem.product = product
#     orderitem.order = order
#     orderitem.quantity = quantity
#     orderitem.save()
#     return orderitem


# @router.delete("/orderitem/{id}", status_code=204)
# def delete_orderitem(id: int):
#     orderitem = OrderItem.objects.get(id=id)
#     orderitem.delete()
#     return None





