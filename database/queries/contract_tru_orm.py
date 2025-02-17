from sqlalchemy import select

from database.models import ContractTRU
from database.superset_models import ContractTRU as SsContractTRU
from database.simbase_database import session_factory
from database.queries.base_orm import BaseOrm


class SsContractTRUOrm(BaseOrm):
    target_model = SsContractTRU


class ContractTRUOrm:
        
    @staticmethod
    def all(**kwargs) -> list[ContractTRU]:
        with session_factory() as session:
            query = select(ContractTRU)
            if kwargs.get('date'):
                query.where(ContractTRU.date == kwargs['date'])
            return session.execute(query).scalars().all()
