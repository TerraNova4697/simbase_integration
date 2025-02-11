from sqlalchemy import select

from database.models import Contract
from database.simbase_database import session_factory
from database.superset_models import Contract as SsContract
from database.queries.base_orm import BaseOrm


class SsContractOrm(BaseOrm):
    target_model = SsContract


class ContractOrm:

    @staticmethod
    def all(**kwargs):
        with session_factory() as session:
            query = select(Contract)
            if dt := kwargs.get('date'):
                query.where(Contract.date == dt)
            return session.execute(query).scalars().all()
    