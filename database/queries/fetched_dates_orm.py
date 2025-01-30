from sqlalchemy import select, and_
from datetime import date

from database.superset_models import FetchedDates
from database.superset_database import superset_session_factory


class FetchedDatesOrm:

    @staticmethod
    def get_last() -> FetchedDates | None:
        with superset_session_factory() as session:
            query = (
                select(
                    FetchedDates
                )
            )
            return session.execute(query).scalar()
        
    @staticmethod
    def create(date: date) -> None:
        with superset_session_factory() as session:
            session.add(FetchedDates(date_created=date))
            session.commit()
