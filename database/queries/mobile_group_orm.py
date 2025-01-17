from sqlalchemy import select

from database.models import MobileGroup
from database.database import session_factory


class MobileGroupOrm:

    @staticmethod
    def insert(**kwargs):
        with session_factory() as session:
            obj = MobileGroup(**kwargs)
            session.add(obj)
            session.commit()
