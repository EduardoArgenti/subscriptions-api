from sqlalchemy.orm import Session
from models.Plan import Plan
from models.Product import Product
from typing import List, Optional
from schemas.Product import ProductCreate
from fastapi import HTTPException
from datetime import datetime

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

def add_products_to_plans(db: Session, id: int, products: List[ProductCreate], mode: str) -> Plan:
    db_plan = db.query(Plan).filter(Plan.id == id).first()

    if not db_plan:
        raise HTTPException(status_code=404, detail=f"Plan with ID {id} not found")

    if mode == "add":
        for product in products:
            db_product = Product(
                name=product.name,
                desc=product.desc,
                plan_id=db_plan.id
            )
            db.add(db_product)
    elif mode == "delete":
        pass
    else:
        raise HTTPException(status_code=400, detail="Invalid mode. Use 'add' or 'delete'.")

    db_plan.updated_at = datetime.utcnow()
    db.add(db_plan)

    db.commit()
    db.refresh(db_plan)

    return db_plan