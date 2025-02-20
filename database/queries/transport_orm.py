from sqlalchemy import select

from database.models import Transport
from database.superset_models import Transport as SsTransport
from database.simbase_database import session_factory
from database.queries.base_orm import BaseOrm


class SsTransportOrm(BaseOrm):
    target_model = SsTransport


class TransportOrm:

    @staticmethod
    def all(**kwargs) -> list[Transport]:
        with session_factory() as session:
            query = (
                select(
                    Transport
                )
            )
            if kwargs.get('date'):
                query.where(Transport.date == kwargs['date'])
            return session.execute(query).scalars().all()