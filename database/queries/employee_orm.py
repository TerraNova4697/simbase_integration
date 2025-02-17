from sqlalchemy import select

from database.models import Employee
from database.superset_models import Employee as SsEmployee
from database.simbase_database import session_factory
from database.queries.base_orm import BaseOrm


class SsEmployeeOrm(BaseOrm):
    target_model = SsEmployee


class EmployeeOrm:
        
    @staticmethod
    def all(**kwargs) -> list[Employee]:
        with session_factory() as session:
            query = select(Employee)
            if kwargs.get('date'):
                query.where(Employee.date == kwargs['date'])
            return session.execute(query).scalars().all()
