from sqlalchemy import select

from database.models import Shift
from database.superset_models import Shift as SsShift
from database.simbase_database import session_factory
from database.queries.base_orm import BaseOrm


class SsShiftOrm(BaseOrm):
    target_model = SsShift


class ShiftOrm:

    @staticmethod
    def all(**kwargs) -> list[Shift]:
        with session_factory() as session:
            query = (
                select(
                    Shift
                )
            )
            if kwargs.get('date'):
                query.where(Shift.date == kwargs['date'])
            return session.execute(query).scalars().all()
