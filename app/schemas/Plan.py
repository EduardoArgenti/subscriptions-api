from pydantic import BaseModel
from datetime import datetime
from schemas.Product import ProductCreate, ProductResponse
from typing import List

class PlanCreate(BaseModel):
    value: float
    products: List[ProductCreate]

class PlanResponse(BaseModel):
    id: int
    value: float
    products: List[ProductResponse]
    active: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True