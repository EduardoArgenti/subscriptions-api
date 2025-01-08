from pydantic import BaseModel

class Plan(BaseModel):
    id: int
    value: float
    #products: list
    # created_at: datetime