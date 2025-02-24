from sqlalchemy import select

from database.models import WeaponAndSpecEquipment
from database.superset_models import WeaponAndSpecEquipment as SsWeaponAndSpecEquipment
from database.simbase_database import session_factory
from database.queries.base_orm import BaseOrm


class SsWeaponAndSpecEquipmentOrm(BaseOrm):
    target_model = SsWeaponAndSpecEquipment


class WeaponAndSpecEquipmentOrm:

    @staticmethod
    def all(**kwargs) -> list[WeaponAndSpecEquipment]:
        with session_factory() as session:
            query = (
                select(
                    WeaponAndSpecEquipment
                )
            )
            if kwargs.get('date'):
                query.where(WeaponAndSpecEquipment.date == kwargs['date'])
            return session.execute(query).scalars().all()
