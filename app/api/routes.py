from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
from fastapi.responses import JSONResponse

from sqlalchemy.orm import Session
from database import get_db

from schemas.Plan import PlanCreate, PlanResponse
from schemas.Product import ProductCreate

from repositories.Plan import PlanRepository
from repositories.Log import save_log

from typing import List

router = APIRouter()

@router.get("/plans/", response_model=List[PlanResponse])
def read_plans_route(
        background_tasks: BackgroundTasks,
        skip: int = 0,
        limit: int = 10,
        db: Session = Depends(get_db)
    ):

    plans = PlanRepository.get_all_plans(db, skip=skip, limit=limit)

    background_tasks.add_task(save_log, db, "GET /plans/", "Fetched plans list", 200)
    return plans

@router.get("/plans/{plan_id}", response_model=PlanResponse)
def read_plan_route(
        background_tasks: BackgroundTasks,
        plan_id: int,
        db: Session = Depends(get_db)
    ):

    plan = PlanRepository.get_plan_by_id(db, plan_id)

    if plan is None:
        raise HTTPException(404, f"Plan {plan_id} not found.")

    background_tasks.add_task(save_log, db, "GET /plans/{plan_id}", f"Fetched plan {plan_id}", 200)
    return plan

@router.post("/plans/", response_model=PlanResponse)
def create_plan_route(
        background_tasks: BackgroundTasks,
        plan: PlanCreate,
        db: Session = Depends(get_db)
    ):

    db_plan = PlanRepository.create_plan_with_products(db, value=plan.value, products=plan.products)

    background_tasks.add_task(save_log, db, "POST /plans/", f"Create plan", 200)
    return db_plan

@router.patch("/plans/{plan_id}/add_products", response_model=PlanResponse)
def add_products_route(
        background_tasks: BackgroundTasks,
        plan_id: int,
        products: List[ProductCreate],
        db: Session = Depends(get_db)
    ):

    db_plan = PlanRepository.add_products_to_plans(db, id=plan_id, products=products)

    background_tasks.add_task(save_log, db, "PATCH /plans/{plan_id}/add_products", f"Add products to plan", 200)
    return db_plan

@router.patch("/plans/{plan_id}/remove_products", response_model=PlanResponse)
def remove_products_route(
        background_tasks: BackgroundTasks,
        plan_id: int,
        products_ids: List[int],
        db: Session = Depends(get_db)
    ):

    db_plan = PlanRepository.remove_products_from_plans(db, id=plan_id, products_ids=products_ids)

    background_tasks.add_task(save_log, db, "PATCH /plans/{plan_id}/remove_products", f"Remove products from plan", 200)
    return db_plan