from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from database.models import Post
from database.superset_models import Post as SsPost
from database.simbase_database import session_factory
from database.queries.base_orm import BaseOrm
from logger import logger


class SsPostOrm(BaseOrm):
    target_model = SsPost


class PostOrm:

    @staticmethod
    def all(**kwargs):
        with session_factory() as session:
            query = select(Post)
            if kwargs.get('date'):
                query.where(Post.date)
            return session.execute(query).scalars().all()

    @staticmethod
    def create(**kwargs):
        with session_factory() as session:
            try:
                obj = Post(**kwargs)
                session.add(obj)
                session.commit()
            except IntegrityError as exc:
                logger.exception(exc)
                raise
            # return obj