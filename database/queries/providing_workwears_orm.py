from sqlalchemy import select

from database.models import ProvidingWorkwears
from database.superset_models import ProvidingWorkwears as SsProvidingWorkwears
from database.simbase_database import session_factory
from database.queries.base_orm import BaseOrm


class SsProvidingWorkwearsOrm(BaseOrm):
    target_model = SsProvidingWorkwears


class ProvidingWorkwearsOrm:

    @staticmethod
    def all(**kwargs) -> list[ProvidingWorkwears]:
        with session_factory() as session:
            query = (
                select(
                    ProvidingWorkwears
                )
            )
            if kwargs.get('date'):
                query.where(ProvidingWorkwears.date == kwargs['date'])
            return session.execute(query).scalars().all()
