from sqlalchemy import select, and_
from datetime import date, timedelta

from database.models import Filial
from database.superset_models import Filial as SsFilial
from database.simbase_database import session_factory
from database.queries.base_orm import BaseOrm


class SsFilialOrm(BaseOrm):
    target_model = SsFilial


class FilialOrm:

    @staticmethod
    def all(**kwargs) -> list[Filial]:
        with session_factory() as session:
            query = (
                select(
                    Filial
                )
            )
            if kwargs.get('date'):
                query.where(Filial.date == kwargs['date'])
            return session.execute(query).scalars().all()

    @staticmethod
    def get_all_by_date(dt: date) -> list[Filial]:
        with session_factory() as session:
            query = (
                select(
                    Filial
                )
                .where(and_(
                    Filial.date >= dt,
                    Filial.date < dt + timedelta(days=1)
                ))
            )
            return session.execute(query).scalars().all()

    @staticmethod
    def insert_filial(**kwargs):
        with session_factory() as session:
            
            session.add(Filial(**kwargs))
            session.commit()


    @staticmethod
    def get_id_sb_object_filials():
        with session_factory() as session:
            query = (
                select(Filial.id_sb_object_filial) \
                    .distinct()
            )
            return session.execute(query).scalars().all()
        
    @staticmethod
    def get_all_filials():
        with session_factory() as session:
            query = (
                select(Filial)
            )
            return session.execute(query).scalars().all()
        
    @staticmethod
    def get_by_sb_id(filial_sb_id):
        with session_factory() as session:
            query = (
                select(Filial).filter(Filial.id_sb_object_filial == filial_sb_id)
            )
            return session.execute(query).scalars().first()
        
