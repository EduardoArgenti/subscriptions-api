from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models.Plan import Plan
from schemas.Plan import PlanCreate, PlanResponse

router = APIRouter()

@router.post("/plans/", response_model=PlanResponse)
def create_plan(plan: PlanCreate, db: Session = Depends(get_db)):
    db_plan = Plan(value=plan.value)
    db.add(db_plan)
    db.commit()
    db.refresh(db_plan)
    return db_plan