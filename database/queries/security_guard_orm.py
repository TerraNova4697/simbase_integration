from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from database.models import SecurityGuard
from database.superset_models import SecurityGuard as SsSecurityGuard, SqlError
from database.simbase_database import session_factory
from database.superset_database import superset_session_factory
from logger import logger
from helper_models import SecurityGuardModel

from traceback import format_exc


class SsSecurityGuardOrm:

    @staticmethod
    def create(**kwargs) -> None:
        with superset_session_factory() as session:
            initial_model = kwargs.pop("model")
            try:
                security_guard = SsSecurityGuard(**kwargs)
                session.add(security_guard)
                session.commit()
            except IntegrityError as exc:
                session.rollback()
                compiled = security_guard.__table__.insert().values(**kwargs).compile(compile_kwargs={"literal_binds": True})
                session.add(SqlError(
                    exception=str(exc.__class__),
                    traceback=format_exc(),
                    sql=str(compiled),
                    target_model=SsSecurityGuard.__name__,
                    source_object=SecurityGuardModel.model_validate(initial_model, from_attributes=True).model_dump(mode="json")
                ))
                session.commit()


class SecurityGuardOrm:

    @staticmethod
    def all(**kwargs):
        with session_factory() as session:
            query = select(SecurityGuard)
            if kwargs.get('date'):
                query.where(SecurityGuard.date)
            return session.execute(query).scalars().all()