from fastapi import HTTPException

from sqlalchemy.orm import Session
from repositories.Plan import PlanRepository

from models.Plan import Plan

from schemas.Plan import PlanResponse
from schemas.Product import ProductCreate

from typing import List

class PlanService:
    @staticmethod
    def fetch_plans_service(db: Session, skip: int = 0, limit: int = 10) -> List[PlanResponse]:
        plans = PlanRepository.get_all_plans(db, skip=skip, limit=limit)
        return plans

    @staticmethod
    def fetch_plan_by_id(db: Session, plan_id: int) -> PlanResponse:
        plan = PlanRepository.get_plan_by_id(db, plan_id)
        if plan is None:
            raise HTTPException(404, f"Plan {plan_id} not found.")
        return plan

    @staticmethod
    def create_plan_with_products(db: Session, value: float, products: List[ProductCreate]) -> Plan:
        plan = PlanRepository.create_plan_with_products(db, value, products)
        return plan

    @staticmethod
    def add_products_to_plan(db: Session, id: int, products: List[ProductCreate]) -> Plan:
        plan = PlanRepository.add_products_to_plan(db, id, products=products)
        return plan

    @staticmethod
    def remove_products_from_plan(db: Session, id: int, products_ids: List[ProductCreate]):
        plan = PlanRepository.remove_products_from_plan(db, id, products_ids)
        return plan