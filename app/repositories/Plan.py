from sqlalchemy.orm import Session
from models.Plan import Plan
from models.Product import Product
from typing import List, Optional
from schemas.Product import ProductCreate
from fastapi import HTTPException
from datetime import datetime

class PlanRepository:
    @staticmethod
    def get_all_plans(db: Session, skip: int = 0, limit: int = 10) -> List[Plan]:
        return db.query(Plan).offset(skip).limit(limit).all()

    @staticmethod
    def get_plan_by_id(db: Session, plan_id: int) -> Optional[Plan]:
        return db.query(Plan).filter(Plan.id == plan_id).first()

    @staticmethod
    def create_plan_with_products(db: Session, value: float, products: List[ProductCreate]) -> Plan:
        db_plan = Plan(value=value)

        db_products = [
            Product(
                name=product.name,
                desc=product.desc,
                plan_id=db_plan.id,
            )
            for product in products
        ]

        db_plan.products = db_products

        db.add(db_plan)
        db.commit()
        db.refresh(db_plan)

        return db_plan

    @staticmethod
    def add_products_to_plans(db: Session, id: int, products: List[ProductCreate]) -> Plan:
        db_plan = db.query(Plan).filter(Plan.id == id).first()

        if not db_plan:
            raise HTTPException(status_code=404, detail=f"Plan with ID {id} not found")

        for product in products:
            db_product = Product(
                name=product.name,
                desc=product.desc,
                plan_id=db_plan.id
            )
            db.add(db_product)

        db_plan.updated_at = datetime.utcnow()
        db.add(db_plan)

        db.commit()
        db.refresh(db_plan)

        return db_plan

    @staticmethod
    def remove_products_from_plans(db: Session, id: int, products_ids: List[int]) -> Plan:
        db_plan = db.query(Plan).filter(Plan.id == id).first()

        if not db_plan:
            raise HTTPException(status_code=404, detail=f"Plan with ID {id} not found")

        for product_id in products_ids:
            db_product = db.query(Product).filter(Product.id == product_id).first()

            if not db_product:
                raise HTTPException(status_code=404, detail=f"Product with ID {product_id} not found")

            if db_product.active == False:
                continue

            db_product.updated_at = datetime.utcnow()
            db_product.active = False
            db.add(db_product)

        db_plan.updated_at = datetime.utcnow()
        db.add(db_plan)

        db.commit()
        db.refresh(db_plan)

        return db_plan