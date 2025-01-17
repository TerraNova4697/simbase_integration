from sqlalchemy import select

from database.models import Filial
from database.database import session_factory


class FilialOrm:

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
        
