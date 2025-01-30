from database.models import Event
from database.simbase_database import session_factory


class EventOrm:

    @staticmethod
    def insert_event(**kwargs):
        with session_factory() as session:
            session.add(Event(**kwargs))
            session.commit()