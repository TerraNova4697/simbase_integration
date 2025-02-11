from pydantic import BaseModel
from traceback import format_exc

from sqlalchemy.exc import IntegrityError

from database.superset_database import superset_session_factory
from database.superset_models import SqlError


class BaseOrm:
    target_model = None

    @classmethod
    def create_from_schema(cls, schema: BaseModel) -> None:
        with superset_session_factory() as session:
            try:
                values = schema.model_dump(exclude={"id"})
                model = cls.target_model(**values)
                session.add(model)
                session.commit()
            except IntegrityError as exc:
                session.rollback()
                compiled = str(model.__table__.insert().values(**values).compile(compile_kwargs={"literal_binds": True}))
                cls.create_sql_error(
                    session=session,
                    exc=str(exc.__class__),
                    sql_query=str(compiled),
                    source_obj=schema.model_dump(mode="json")
                )

    @classmethod
    def create_sql_error(cls, session, exc: str, sql_query: str, source_obj):
        session.add(SqlError(
            exception=exc,
            traceback=format_exc(),
            sql=sql_query,
            target_model=cls.target_model.__name__,
            source_object=source_obj)
        )
        session.commit()
        