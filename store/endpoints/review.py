from fastapi import APIRouter
from store.models import Review
from store.schemas.review import ReviewSchema
from typing import List

router = APIRouter()



@router.get("/review", response_model=List[ReviewSchema], status_code=200)
def get_reviews():
    reviews = Review.objects.all()
    return [ReviewSchema.from_django(review) for review in reviews]

# @router.post("/review", response_model=ReviewSchema, status_code=201)
# def create_review(product: int, user: int, rating: int, review: str):
#     review = Review.objects.create()
#     review.product = product
#     review.user = user
#     review.rating = rating
#     review.review = review
#     review.save()
#     return review

# @router.put("/review/{id}", response_model=ReviewSchema, status_code=200)
# def update_review(id: int, product: int, user: int, rating: int, review: str):
#     review = Review.objects.get(id=id)
#     review.product = product
#     review.user = user
#     review.rating = rating
#     review.review = review
#     review.save()
#     return review

# @router.delete("/review/{id}", status_code=204)
# def delete_review(id: int):
#     review = Review.objects.get(id=id)
#     review.delete()
#     return None
