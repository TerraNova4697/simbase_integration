import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

from config.settings import settings


engine_east = create_engine(settings.database_url_east, connect_args={'options': '-csearch_path=dbo'})
engine_west = create_engine(settings.database_url_west, connect_args={'options': '-csearch_path=dbo'})

session_factory_east = sessionmaker(bind=engine_east)
session_factory_west = sessionmaker(bind=engine_west)


class Base(DeclarativeBase):
    repr_cols_num = 3
    repr_cols = tuple()

    def __repr__(self):
        cols = []
        for idx, col in enumerate(self.__table__.columns.keys()):
            if col in self.repr_cols or idx < self.repr_cols_num:
                cols.append(f"{col}={getattr(self, col)}")

        return f"<{self.__class__.__name__} {', '.join(cols)}>"
