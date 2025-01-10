from sqlalchemy import Column, Integer, String, DateTime
from database import Base
from datetime import datetime

class Log(Base):
    __tablename__ = 'logs'

    id = Column(Integer, primary_key=True, index=True)
    route = Column(String, index=True)
    message = Column(String)
    status_code = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)