from sqlalchemy import select

from database.models import Triggering
from database.superset_models import Triggering as SsTriggering
from database.simbase_database import session_factory
from database.queries import BaseOrm


class SsTriggeringOrm(BaseOrm):
    target_model = SsTriggering


class TriggeringOrm:

    @staticmethod
    def all(**kwargs):
        with session_factory() as session:
            query = select(Triggering)
            if dt := kwargs.get('date'):
                query.where(Triggering.date == dt)
            return session.execute(query).scalars().all()
    