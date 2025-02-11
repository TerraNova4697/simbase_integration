from sqlalchemy import select, and_
from datetime import date, timedelta

from database.models import Customer
from database.superset_models import Customer as SsCustomer
from database.simbase_database import session_factory
from database.queries.base_orm import BaseOrm


class SsCustomerOrm(BaseOrm):
    target_model = SsCustomer


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
