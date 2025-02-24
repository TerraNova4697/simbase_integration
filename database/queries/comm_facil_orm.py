from sqlalchemy import select

from database.models import CommunicationFacilitiy
from database.superset_models import CommunicationFacilitiy as SsCommunicationFacilitiy
from database.simbase_database import session_factory
from database.queries.base_orm import BaseOrm


class SsCommunicationFacilitiyOrm(BaseOrm):
    target_model = SsCommunicationFacilitiy


class CommunicationFacilitiyOrm:

    @staticmethod
    def all(**kwargs) -> list[CommunicationFacilitiy]:
        with session_factory() as session:
            query = (
                select(
                    CommunicationFacilitiy
                )
            )
            if kwargs.get('date'):
                query.where(CommunicationFacilitiy.date == kwargs['date'])
            return session.execute(query).scalars().all()
