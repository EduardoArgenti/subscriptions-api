from fastapi import APIRouter, Depends, BackgroundTasks

from sqlalchemy.orm import Session
from database import get_db

from schemas.Plan import PlanCreate, PlanResponse
from schemas.Product import ProductCreate

from repositories.Log import save_log

from services.Plan import PlanService

from typing import List

from auth import authenticate

router = APIRouter()

@router.get("/plans/", tags=["Plans"], response_model=List[PlanResponse])
def read_plans_route(
        background_tasks: BackgroundTasks,
        skip: int = 0,
        limit: int = 10,
        db: Session = Depends(get_db),
        _: None = Depends(authenticate)
    ):

    plans = PlanService.fetch_plans_service(db, skip=skip, limit=limit)

    background_tasks.add_task(save_log, db, "GET /plans/", "Fetched plans list", 200)

    return plans

@router.get("/plans/{plan_id}",  tags=["Plans"], response_model=PlanResponse)
def read_plan_route(
        background_tasks: BackgroundTasks,
        plan_id: int,
        db: Session = Depends(get_db),
        _: None = Depends(authenticate)
    ):

    plan = PlanService.fetch_plan_by_id(db, plan_id)

    background_tasks.add_task(save_log, db, "GET /plans/{plan_id}", f"Fetched plan {plan_id}", 200)
    return plan

@router.post("/plans/", tags=["Plans"], response_model=PlanResponse)
def create_plan_route(
        background_tasks: BackgroundTasks,
        plan: PlanCreate,
        db: Session = Depends(get_db),
        _: None = Depends(authenticate)
    ):

    created_plan = PlanService.create_plan_with_products(db, value=plan.value, products=plan.products)

    background_tasks.add_task(save_log, db, "POST /plans/", f"Create plan", 200)
    return created_plan

@router.patch("/plans/{plan_id}/add_products", tags=["Plans"], response_model=PlanResponse)
def add_products_route(
        background_tasks: BackgroundTasks,
        plan_id: int,
        products: List[ProductCreate],
        db: Session = Depends(get_db),
        _: None = Depends(authenticate)
    ):

    updated_plan = PlanService.add_products_to_plan(db, id=plan_id, products=products)

    background_tasks.add_task(save_log, db, "PATCH /plans/{plan_id}/add_products", f"Add products to plan", 200)
    return updated_plan

@router.patch("/plans/{plan_id}/remove_products", tags=["Plans"], response_model=PlanResponse)
def remove_products_route(
        background_tasks: BackgroundTasks,
        plan_id: int,
        products_ids: List[int],
        db: Session = Depends(get_db),
        _: None = Depends(authenticate)
    ):

    updated_plan = PlanService.remove_products_from_plan(db, id=plan_id, products_ids=products_ids)

    background_tasks.add_task(save_log, db, "PATCH /plans/{plan_id}/remove_products", f"Remove products from plan", 200)
    return updated_plan