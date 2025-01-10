from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from repositories.plan_repository import create_plan_with_products, get_all_plans, get_plan_by_id, add_products_to_plans, remove_products_from_plans
from schemas.Plan import PlanCreate, PlanResponse
from schemas.Product import ProductCreate
from typing import List

router = APIRouter()

@router.get("/plans/", response_model=List[PlanResponse])
def read_plans_route(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    plans = get_all_plans(db, skip=skip, limit=limit)
    return plans

@router.get("/plans/{plan_id}", response_model=PlanResponse)
def read_plan_route(plan_id: int, db: Session = Depends(get_db)):
    plan = get_plan_by_id(db, plan_id)
    if plan is None:
        raise HTTPException(status_code=404, detail=f"Plan not found")
    return plan

@router.post("/plans/", response_model=PlanResponse)
def create_plan_route(plan: PlanCreate, db: Session = Depends(get_db)):
    db_plan = create_plan_with_products(db, value=plan.value, products=plan.products)
    return db_plan

@router.patch("/plans/{plan_id}/add_products", response_model=PlanResponse)
def add_products_route(plan_id: int, products: List[ProductCreate], db: Session = Depends(get_db)):
    db_plan = add_products_to_plans(db, id=plan_id, products=products)
    return db_plan

@router.patch("/plans/{plan_id}/remove_products", response_model=PlanResponse)
def remove_products_route(plan_id: int, products_ids: List[int], db: Session = Depends(get_db)):
    db_plan = remove_products_from_plans(db, id=plan_id, products_ids=products_ids)
    return db_plan