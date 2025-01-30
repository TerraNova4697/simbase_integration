from sqlalchemy import select, and_, insert
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import joinedload
from datetime import date, timedelta
from traceback import format_exc

from database.models import Filial
from database.superset_models import Filial as SsFilial, SqlError
from database.simbase_database import session_factory
from database.superset_database import superset_session_factory
from logger import logger
from helper_models import FilialModel


class SsFilialOrm:

    @staticmethod
    def get_by_sb_id(sb_filial_id) -> bool:
        with superset_session_factory() as session:
            query = (
                select(
                    Filial
                ).exists()
            )
            return session.execute(query)
        
    @staticmethod
    def create(**kwargs) -> None:
        with superset_session_factory() as session:
            initial_model = kwargs.pop("model")
            try:
                filial = SsFilial(**kwargs)
                session.add(filial)
                session.commit()
            except IntegrityError as exc:
                session.rollback()
                compiled = filial.__table__.insert().values(**kwargs).compile(compile_kwargs={"literal_binds": True})
                session.add(SqlError(
                    exception=str(exc.__class__),
                    traceback=format_exc(),
                    sql=str(compiled),
                    target_model=SsFilial.__name__,
                    source_object=FilialModel.model_validate(initial_model, from_attributes=True).model_dump(mode="json")
                ))
                session.commit()

    @staticmethod
    def first() -> SsFilial:
        with superset_session_factory() as session:
            try:
                query = (
                    select(SsFilial)
                        .options(joinedload(SsFilial.customers))
                        .limit(1)
                )
                return session.execute(query).scalar()
            except IntegrityError as exc:
                logger.exception(exc)


class FilialOrm:

    @staticmethod
    def all(**kwargs) -> list[Filial]:
        with session_factory() as session:
            query = (
                select(
                    Filial
                )
            )
            if kwargs.get('date'):
                query.where(Filial.date == kwargs['date'])
            return session.execute(query).scalars().all()

    @staticmethod
    def get_all_by_date(dt: date) -> list[Filial]:
        with session_factory() as session:
            query = (
                select(
                    Filial
                )
                .where(and_(
                    Filial.date >= dt,
                    Filial.date < dt + timedelta(days=1)
                ))
            )
            return session.execute(query).scalars().all()

    @staticmethod
    def insert_filial(**kwargs):
        with session_factory() as session:
            
            session.add(Filial(**kwargs))
            session.commit()


    @staticmethod
    def get_id_sb_object_filials():
        with session_factory() as session:
            query = (
                select(Filial.id_sb_object_filial) \
                    .distinct()
            )
            return session.execute(query).scalars().all()
        
    @staticmethod
    def get_all_filials():
        with session_factory() as session:
            query = (
                select(Filial)
            )
            return session.execute(query).scalars().all()
        
    @staticmethod
    def get_by_sb_id(filial_sb_id):
        with session_factory() as session:
            query = (
                select(Filial).filter(Filial.id_sb_object_filial == filial_sb_id)
            )
            return session.execute(query).scalars().first()
        
