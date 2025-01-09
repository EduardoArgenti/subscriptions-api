from pydantic import BaseModel
from schemas.Product import ProductCreate, ProductResponse
from typing import List

class PlanCreate(BaseModel):
    value: float
    products: List[ProductCreate]

class PlanResponse(BaseModel):
    id: int
    value: float
    products: List[ProductResponse]

    class Config:
        orm_mode = True