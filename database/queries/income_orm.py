from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from database.models import Income
from database.superset_models import Income as SsIncome, SqlError
from database.simbase_database import session_factory
from database.superset_database import superset_session_factory
from helper_models import IncomeModel

from traceback import format_exc


class SsIncomeOrm:

    @staticmethod
    def create(**kwargs) -> None:
        with superset_session_factory() as session:
            initial_model = kwargs.pop('model')
            # try:
            income = SsIncome(**kwargs)
            session.add(income)
            session.commit()
            # except IntegrityError as exc:
            #     session.rollback()
            #     compiled = income.__table__.insert().values(**kwargs).compile(compile_kwargs={"literal_binds": True})
            #     session.add(SqlError(
            #         exception=str(exc.__class__),
            #         traceback=format_exc(),
            #         sql=str(compiled),
            #         target_model=SsIncome.__name__,
            #         source_object=IncomeModel.model_validate(
            #             initial_model,
            #             from_attributes=True
            #         ).model_dump(mode="json")
            #     ))
            #     session.commit()


class IncomeOrm:

    @staticmethod
    def all(**kwargs):
        with session_factory() as session:
            query = select(Income)
            if dt := kwargs.get('date'):
                query.where(Income.date == dt)
            return session.execute(query).scalars().all()

    @staticmethod
    def insert(**kwargs):
        with session_factory() as session:
            session.add(Income(**kwargs))
            session.commit()