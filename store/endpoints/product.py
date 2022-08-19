from typing import List
from enum import Enum
from datetime import datetime
from django.core.files import File as DjangoFile
from fastapi import APIRouter, UploadFile, Form
from store.models import Product
from store.schemas.product import ProductSchema


router = APIRouter()
  
class CategoryChoices(str, Enum):
    HAIR = "HAIR"
    SKIN = "SKIN CARE"
    MAKEUP = "MAKEUP"
    PERFUME = "PERFUME"
    SOAP = "SOAP"
    HAIR_PRODUCT = "HAIR PRODUCT"

@router.get("/product", response_model=List[ProductSchema], status_code=200)
def get_products():
    products = Product.objects.all()
    return [ProductSchema.from_django(product) for product in products]

@router.post("/product", response_model=ProductSchema, status_code=201)
def create_product(image: UploadFile = Form(...), description: str = Form(...), name: str = Form(...), price: float = Form(...), category: CategoryChoices = Form(...), stock: int = Form(...)):
    product = Product.objects.create()
    product.name = name
    product.description = description
    product.price = price
    product.category = category
    product.stock = stock
    product.image = DjangoFile(image.file, name=image.filename)
    product.save()
    return product

@router.put("/product/{id}", response_model=ProductSchema, status_code=200)
def update_product(id: int, image: UploadFile = Form(...), description: str = Form(...) , name: str = Form(...), price: float = Form(...), category: CategoryChoices = Form(...), stock: int = Form(...)):
    product = Product.objects.get(id=id)
    product.name = name
    product.description = description
    product.price = price
    product.category = category
    product.stock = stock
    product.image = DjangoFile(image.file, name=image.filename)
    product.save()
    return product

@router.delete("/product/{id}", status_code=204)
def delete_product(id: int):
    product = Product.objects.get(id=id)
    product.delete()
    return None