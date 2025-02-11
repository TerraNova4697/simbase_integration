from sqlalchemy import select

from database.models import Object
from database.superset_models import Object as SsObject
from database.simbase_database import session_factory
from database.queries.base_orm import BaseOrm


class SsObjectOrm(BaseOrm):
    target_model = SsObject


class ObjectOrm:

    @staticmethod
    def insert_object(**kwargs):
        with session_factory() as session:
            obj = Object(**kwargs)
            session.add(obj)
            session.commit()
            return obj
        
    @staticmethod
    def all(**kwargs):
        with session_factory() as session:
            query = (
                select(Object)
            )
            if kwargs.get('date'):
                query.where(Object.date == kwargs['date'])
            return session.execute(query).scalars().all()
