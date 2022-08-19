from fastapi import APIRouter
from .endpoints import product, review, order, orderitem, shipping


router = APIRouter()


router.include_router(product.router, prefix="/product", tags=["product"])
router.include_router(review.router, prefix="/review", tags=["review"])
router.include_router(order.router, prefix="/order", tags=["order"])
router.include_router(orderitem.router, prefix="/orderitem", tags=["orderitem"])
router.include_router(shipping.router, prefix="/shipping", tags=["shipping"])





