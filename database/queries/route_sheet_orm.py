from sqlalchemy import select

from database.models import RouteSheet
from database.simbase_database import session_factory


class RouteSheetOrm:

    @staticmethod
    def insert_object(**kwargs):
        with session_factory() as session:
            obj = RouteSheet(**kwargs)
            session.add(obj)
            session.commit()
            return obj
        
    @staticmethod
    def all(**kwargs):
        with session_factory() as session:
            query = (
                select(RouteSheet)
            )
            if kwargs.get('date'):
                query.where(RouteSheet.date == kwargs['date'])
            return session.execute(query).scalars().all()
