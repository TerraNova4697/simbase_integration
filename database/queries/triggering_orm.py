from sqlalchemy import select, and_, insert
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import joinedload
from datetime import date, timedelta
from traceback import format_exc

from database.models import Triggering
from database.superset_models import Triggering as SsTriggering, SqlError
from database.simbase_database import session_factory
from database.superset_database import superset_session_factory
from logger import logger
from helper_models import TriggeringModel


class SsTriggeringOrm:

    @staticmethod
    def get_by_sb_id(sb_filial_id) -> bool:
        with superset_session_factory() as session:
            query = (
                select(
                    SsTriggering
                ).exists()
            )
            return session.execute(query)
        
    @staticmethod
    def create(**kwargs) -> None:
        with superset_session_factory() as session:
            initial_model = kwargs.pop("model")
            try:
                contract = SsTriggering(**kwargs)
                session.add(contract)
                session.commit()
            except IntegrityError as exc:
                session.rollback()
                compiled = contract.__table__.insert().values(**kwargs).compile(compile_kwargs={"literal_binds": True})
                session.add(SqlError(
                    exception=str(exc.__class__),
                    traceback=format_exc(),
                    sql=str(compiled),
                    target_model=SsTriggering.__name__,
                    source_object=TriggeringModel.model_validate(initial_model, from_attributes=True).model_dump(mode="json")
                ))
                session.commit()

    @staticmethod
    def create_from_schema(schema: TriggeringModel) -> None:
        with superset_session_factory() as session:
            try:
                values = schema.model_dump(exclude={"id"})
                model = SsTriggering(**values)
                session.add(model)
                session.commit()
            except IntegrityError as exc:
                session.rollback()
                compiled = model.__table__.insert().values(**values).compile(compile_kwargs={"literal_binds": True})
                session.add(SqlError(
                    exception=str(exc.__class__),
                    traceback=format_exc(),
                    sql=str(compiled),
                    target_model=SsTriggering.__name__,
                    source_object=schema.model_dump(mode="json")
                ))

    @staticmethod
    def first() -> SsTriggering:
        with superset_session_factory() as session:
            try:
                query = (
                    select(SsTriggering)
                        .options(joinedload(SsTriggering.customers))
                        .limit(1)
                )
                return session.execute(query).scalar()
            except IntegrityError as exc:
                logger.exception(exc)


class TriggeringOrm:

    @staticmethod
    def all(**kwargs):
        with session_factory() as session:
            query = select(Triggering)
            if dt := kwargs.get('date'):
                query.where(Triggering.date == dt)
            return session.execute(query).scalars().all()
    