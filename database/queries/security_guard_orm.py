from sqlalchemy import select

from database.models import SecurityGuard
from database.superset_models import SecurityGuard as SsSecurityGuard
from database.simbase_database import session_factory
from database.queries.base_orm import BaseOrm


class SsSecurityGuardOrm(BaseOrm):
    target_model = SsSecurityGuard


class SecurityGuardOrm:

    @staticmethod
    def all(**kwargs):
        with session_factory() as session:
            query = select(SecurityGuard)
            if kwargs.get('date'):
                query.where(SecurityGuard.date)
            return session.execute(query).scalars().all()