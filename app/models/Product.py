from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime
from database import Base
from datetime import datetime


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String)
    desc = Column(String)
    plan_id = Column(Integer, ForeignKey("plans.id"), nullable=False)
    active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)