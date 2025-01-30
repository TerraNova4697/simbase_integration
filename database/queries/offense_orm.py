from database.models import Offense
from database.simbase_database import session_factory


class OffenseOrm:

    @staticmethod
    def insert_offense(**kwargs):
        with session_factory() as session:
            session.add(Offense(**kwargs))
            session.commit()