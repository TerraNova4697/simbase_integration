from sqlalchemy import select

from database.models import Income
from database.database import session_factory


class IncomeOrm:

    @staticmethod
    def insert(**kwargs):
        with session_factory() as session:
            session.add(Income(**kwargs))
            session.commit()