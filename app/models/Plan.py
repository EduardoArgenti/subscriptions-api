from sqlalchemy import Column, Integer, Boolean, Float, DateTime
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime

class Plan(Base):
    __tablename__ = "plans"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    value = Column(Float, index=True)
    products = relationship("Product", backref="plan")
    active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)