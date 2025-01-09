from sqlalchemy.orm import Session
from models.Plan import Plan
from typing import List, Optional

def create_plan(db: Session, value: float) -> Plan:
    db_plan = Plan(value=value)
    db.add(db_plan)
    db.commit()
    db.refresh(db_plan)
    return db_plan

def get_all_plans(db: Session, skip: int = 0, limit: int = 10) -> List[Plan]:
    return db.query(Plan).offset(skip).limit(limit).all()

def get_plan_by_id(db: Session, plan_id: int) -> Optional[Plan]:
    return db.query(Plan).filter(Plan.id == plan_id).first()