from sqlalchemy import select, and_, insert
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import joinedload
from datetime import date, timedelta
from traceback import format_exc

from database.models import Triggering
from database.superset_models import Triggering as SsTriggering, SqlError
from database.simbase_database import session_factory
from database.superset_database import superset_session_factory
from database.queries import BaseOrm
from logger import logger
from helper_models import TriggeringModel


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
    