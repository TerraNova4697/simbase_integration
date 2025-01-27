from sqlalchemy import select, and_
from datetime import date

from database.models import FetchedDates
from database.database import session_factory


class FetchedDatesOrm:

    @staticmethod
    def get_last() -> FetchedDates | None:
        with session_factory() as session:
            query = (
                select(
                    FetchedDates
                )
            )
            return session.execute(query).scalar()
        
    @staticmethod
    def create(date: date) -> None:
        with session_factory() as session:
            session.add(FetchedDates(date_created=date))
            session.commit()
