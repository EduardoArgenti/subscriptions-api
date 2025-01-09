from sqlalchemy import Column, Integer, String, Float, ForeignKey
from database import Base

class Plan(Base):
    __tablename__ = "plans"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    value = Column(Float, index=True)