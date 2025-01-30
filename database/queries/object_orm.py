from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from database.models import Object
from database.superset_models import Object as SsObject, SqlError
from database.simbase_database import session_factory
from database.superset_database import superset_session_factory
from logger import logger
from traceback import format_exc
from helper_models import ObjectModel


class SsObjectOrm:

    @staticmethod
    def create(**kwargs) -> None:
        with superset_session_factory() as session:
            initial_model = kwargs.pop("model")
            try:
                object = SsObject(**kwargs)
                session.add(object)
                session.commit()
            except IntegrityError as exc:
                session.rollback()
                compiled = object.__table__.insert().values(**kwargs).compile(compile_kwargs={"literal_binds": True})
                session.add(SqlError(
                    exception=str(exc.__class__),
                    traceback=format_exc(),
                    sql=str(compiled),
                    target_model=SsObject.__name__,
                    source_object=ObjectModel.model_validate(initial_model, from_attributes=True).model_dump(mode="json")
                ))
                session.commit()


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
