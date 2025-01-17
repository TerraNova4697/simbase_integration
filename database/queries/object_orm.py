from sqlalchemy import select

from database.models import Object
from database.database import session_factory


class ObjectOrm:

    @staticmethod
    def insert_object(**kwargs):
        with session_factory() as session:
            obj = Object(**kwargs)
            session.add(obj)
            session.commit()
            return obj
        
    @staticmethod
    def get_all():
        with session_factory() as session:
            query = (
                select(Object)
            )
            return session.execute(query).scalars().all()
