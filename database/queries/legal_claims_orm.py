from sqlalchemy import select

from database.models import LegalClaims
from database.superset_models import LegalClaims as SsLegalClaims
from database.simbase_database import session_factory
from database.queries.base_orm import BaseOrm


class SsLegalClaimsOrm(BaseOrm):
    target_model = SsLegalClaims


class LegalClaimsOrm:

    @staticmethod
    def all(**kwargs) -> list[LegalClaims]:
        with session_factory() as session:
            query = (
                select(
                    LegalClaims
                )
            )
            if kwargs.get('date'):
                query.where(LegalClaims.date == kwargs['date'])
            return session.execute(query).scalars().all()
