from sqlalchemy import select, and_
from sqlalchemy.exc import IntegrityError
from datetime import date, timedelta

from database.models import Customer
from database.superset_models import Customer as SsCustomer, SqlError
from database.simbase_database import session_factory
from database.superset_database import superset_session_factory
from logger import logger
from traceback import format_exc
from helper_models import CustomerModel


class SsCustomerOrm:

    @staticmethod
    def create(**kwargs) -> None:
        with superset_session_factory() as session:
            initial_model = kwargs.pop("model")
            try:
                customer = SsCustomer(**kwargs)
                session.add(customer)
                session.commit()
            except IntegrityError as exc:
                session.rollback()
                compiled = customer.__table__.insert().values(**kwargs).compile(compile_kwargs={"literal_binds": True})
                session.add(SqlError(
                    exception=str(exc.__class__),
                    traceback=format_exc(),
                    sql=str(compiled),
                    target_model=SsCustomer.__name__,
                    source_object=CustomerModel.model_validate(initial_model, from_attributes=True).model_dump(mode="json")
                ))
                session.commit()


class CustomerOrm:

    @staticmethod
    def get_all_by_date(dt: date) -> list[Customer]:
        with session_factory() as session:
            query = (
                select(
                    Customer
                )
                .where(and_(
                    Customer.date >= dt,
                    Customer.date < dt + timedelta(days=1)
                ))
            )
            return session.execute(query).scalars().all()
        
    @staticmethod
    def all(**kwargs) -> list[Customer]:
        with session_factory() as session:
            query = select(Customer)
            if kwargs.get('date'):
                query.where(Customer.date == kwargs['date'])
            return session.execute(query).scalars().all()

    @staticmethod
    def insert_customer(**kwargs):
        with session_factory() as session:
            session.add(Customer(**kwargs))
            session.commit()

    @staticmethod
    def get_customers_by_filial(id_sb_filial):
        with session_factory() as session:
            query = (
                select(Customer) \
                    .filter(Customer.id_sb_object_filial == id_sb_filial)
            )
            return session.execute(query).scalars().all()
        
    @staticmethod
    def get_all():
        with session_factory() as session:
            query = (
                select(Customer) \
            )
            return session.execute(query).scalars().all()
