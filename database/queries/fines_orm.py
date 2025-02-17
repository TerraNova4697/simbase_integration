from sqlalchemy import select

from database.models import Fine
from database.superset_models import Fine as SsFine
from database.simbase_database import session_factory
from database.queries.base_orm import BaseOrm


class SsFineOrm(BaseOrm):
    target_model = SsFine


class FineOrm:

    @staticmethod
    def all(**kwargs) -> list[Fine]:
        with session_factory() as session:
            query = (
                select(
                    Fine
                )
            )
            if kwargs.get('date'):
                query.where(Fine.date == kwargs['date'])
            return session.execute(query).scalars().all()
