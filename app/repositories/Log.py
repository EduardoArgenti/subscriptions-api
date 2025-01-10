from sqlalchemy.orm import Session
from models.Log import Log
from datetime import datetime

def save_log(db: Session, route: str, message: str, status_code: int):
    log_entry = Log(
        route=route,
        message=message,
        status_code=status_code,
        created_at=datetime.utcnow()
    )
    db.add(log_entry)
    db.commit()
    db.refresh(log_entry)
    return log_entry