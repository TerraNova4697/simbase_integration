from database.models import Incident
from database.database import session_factory


class IncidentOrm:

    @staticmethod
    def insert_incident(**kwargs):
        with session_factory() as session:
            session.add(Incident(**kwargs))
            session.commit()
            