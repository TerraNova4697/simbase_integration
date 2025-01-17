from sqlalchemy import select

from database.models import Object
from database.database import session_factory


class ObjectOrm:

    @staticmethod
    def insert_object(**kwargs):
        with session_factory() as session:
            session.add(Object(**kwargs))
            session.commit()