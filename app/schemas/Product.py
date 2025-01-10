from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ProductCreate(BaseModel):
    name: str
    desc: Optional[str] = None

class ProductResponse(BaseModel):
    id: int
    name: str
    desc: Optional[str]
    active: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True