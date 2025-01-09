from pydantic import BaseModel

class ProductCreate(BaseModel):
    name: str
    desc: str

class ProductResponse(BaseModel):
    id: int
    name: str
    desc: str

    class Config:
        orm_mode = True