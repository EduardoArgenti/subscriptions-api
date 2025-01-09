from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String)
    description = Column(String)
    plan_id = Column(Integer, ForeignKey("plans.id"))