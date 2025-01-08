from models.entity import Plan

class PlanRepository:
    def __init__(self):
        self.plans = [
            Plan(id=1, value=74.30),
            Plan(id=2, value=99.99),
        ]

    def get_all_plans(self):
        return self.plans

    def get_plan_by_id(self, plan_id: int):
        pass