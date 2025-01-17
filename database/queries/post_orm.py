from sqlalchemy import select

from database.models import Post
from database.database import session_factory


class PostOrm:

    @staticmethod
    def insert(**kwargs):
        with session_factory() as session:
            obj = Post(**kwargs)
            session.add(obj)
            session.commit()
            # return obj