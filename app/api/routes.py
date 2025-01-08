from fastapi import APIRouter, HTTPException
from services.plan_service import PlanService
from repositories.plan_repository import PlanRepository

router = APIRouter()

plan_repository = PlanRepository()
plan_service = PlanService(plan_repository)

@router.get("/plans")
def get_plans():
    return plan_service.list_plans()

@router.get("/plan/{plan_id}")
def get_plan(plan_id: int):
    plan = plan_service.find_plan(plan_id)
    if not plan:
        raise HTTPException(status_code=404, detail="Plan not found")
    return plan
