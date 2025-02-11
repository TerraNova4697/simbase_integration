from sqlalchemy import select, and_, insert
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import joinedload
from datetime import date, timedelta
from traceback import format_exc

from database.models import Contract
from database.superset_models import Contract as SsContract, SqlError
from database.simbase_database import session_factory
from database.superset_database import superset_session_factory
from logger import logger
from helper_models import ContractModel


class SsContractOrm:

    @staticmethod
    def get_by_sb_id(sb_filial_id) -> bool:
        with superset_session_factory() as session:
            query = (
                select(
                    SsContract
                ).exists()
            )
            return session.execute(query)
        
    @staticmethod
    def create(**kwargs) -> None:
        with superset_session_factory() as session:
            initial_model = kwargs.pop("model")
            try:
                contract = SsContract(**kwargs)
                session.add(contract)
                session.commit()
            except IntegrityError as exc:
                session.rollback()
                compiled = contract.__table__.insert().values(**kwargs).compile(compile_kwargs={"literal_binds": True})
                session.add(SqlError(
                    exception=str(exc.__class__),
                    traceback=format_exc(),
                    sql=str(compiled),
                    target_model=SsContract.__name__,
                    source_object=ContractModel.model_validate(initial_model, from_attributes=True).model_dump(mode="json")
                ))
                session.commit()

    @staticmethod
    def first() -> SsContract:
        with superset_session_factory() as session:
            try:
                query = (
                    select(SsContract)
                        .options(joinedload(SsContract.customers))
                        .limit(1)
                )
                return session.execute(query).scalar()
            except IntegrityError as exc:
                logger.exception(exc)


class ContractOrm:

    @staticmethod
    def all(**kwargs):
        with session_factory() as session:
            query = select(Contract)
            if dt := kwargs.get('date'):
                query.where(Contract.date == dt)
            return session.execute(query).scalars().all()
    