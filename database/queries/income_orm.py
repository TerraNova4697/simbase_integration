from sqlalchemy import select

from database.models import Income
from database.superset_models import Income as SsIncome
from database.simbase_database import session_factory
from database.queries.base_orm import BaseOrm


class SsIncomeOrm(BaseOrm):
    target_model = SsIncome


class IncomeOrm:

    @staticmethod
    def all(**kwargs):
        with session_factory() as session:
            query = select(Income)
            if dt := kwargs.get('date'):
                query.where(Income.date == dt)
            return session.execute(query).scalars().all()

    @staticmethod
    def insert(**kwargs):
        with session_factory() as session:
            session.add(Income(**kwargs))
            session.commit()