from pydantic import BaseModel
from typing import List

class PlanCreate(BaseModel):
    value: float

class PlanResponse(BaseModel):
    id: int
    value: float

    class Config:
        orm_mode = True