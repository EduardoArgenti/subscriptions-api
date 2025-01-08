from repositories.plan_repository import PlanRepository

class PlanService:
    def __init__(self, plan_repository: PlanRepository):
        self.plan_repository = plan_repository

    def list_plans(self):
        return self.plan_repository.get_all_plans()

    def find_plan(self, plan_id: int):
        return self.plan_repository.get_plan_by_id(plan_id)
