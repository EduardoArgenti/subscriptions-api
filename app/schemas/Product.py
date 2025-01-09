from pydantic import BaseModel
from datetime import datetime

class ProductCreate(BaseModel):
    name: str
    desc: str

class ProductResponse(BaseModel):
    id: int
    name: str
    desc: str
    active: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True