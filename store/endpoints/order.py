from fastapi import APIRouter
from store.models import Order
from store.schemas.order import OrderSchema
from typing import List

router = APIRouter()


@router.get("/order", response_model=List[OrderSchema], status_code=200)
def get_orders():
    orders = Order.objects.all()
    return [OrderSchema.from_django(order) for order in orders]

# @router.post("/order", response_model=OrderSchema, status_code=201)
# def create_order(user: int, product: int, quantity: int, order_shipping: str, total: float, tax: float, is_paid: bool, is_delivered: bool, payment_method: str):
#     order = Order.objects.create()
#     order.user = user
#     order.product = product
#     order.quantity = quantity
#     order.order_shipping = order_shipping
#     order.total = total
#     order.tax = tax
#     order.is_paid = is_paid
#     order.is_delivered = is_delivered
#     order.payment_method = payment_method
#     order.save()
#     return order

# @router.put("/order/{id}", response_model=OrderSchema, status_code=200)
# def update_order(id: int, user: int, product: int, quantity: int, order_shipping: str, total: float, tax: float, is_paid: bool, is_delivered: bool, payment_method: str):
#     order = Order.objects.get(id=id)
#     order.user = user
#     order.product = product
#     order.quantity = quantity
#     order.order_shipping = order_shipping
#     order.total = total
#     order.tax = tax
#     order.is_paid = is_paid
#     order.is_delivered = is_delivered
#     order.payment_method = payment_method
#     order.save()
#     return order

# @router.delete("/order/{id}", status_code=204)
# def delete_order(id: int):
#     order = Order.objects.get(id=id)
#     order.delete()
#     return None