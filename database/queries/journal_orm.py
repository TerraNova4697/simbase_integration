from sqlalchemy import select

from database.models import Journal
from database.superset_models import Journal as SsJournal
from database.simbase_database import session_factory
from database.queries.base_orm import BaseOrm


class SsJournalOrm(BaseOrm):
    target_model = SsJournal


class JournalOrm:

    @staticmethod
    def all(**kwargs) -> list[Journal]:
        with session_factory() as session:
            query = (
                select(
                    Journal
                )
            )
            if kwargs.get('date'):
                query.where(Journal.date == kwargs['date'])
            return session.execute(query).scalars().all()