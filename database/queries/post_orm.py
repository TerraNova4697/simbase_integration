from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from database.models import Post
from database.superset_models import Post as SsPost, SqlError
from database.simbase_database import session_factory
from database.superset_database import superset_session_factory
from logger import logger
from helper_models import PostModel

from traceback import format_exc


class SsPostOrm:

    @staticmethod
    def create(**kwargs):
        with superset_session_factory() as session:
            initial_model = kwargs.pop("model")
            try:
                obj = SsPost(**kwargs)
                session.add(obj)
                session.commit()
            except IntegrityError as exc:
                session.rollback()
                compiled = obj.__table__.insert().values(**kwargs).compile(compile_kwargs={"literal_binds": True})
                session.add(SqlError(
                    exception=str(exc.__class__),
                    traceback=format_exc(),
                    sql=str(compiled),
                    target_model=SsPost.__name__,
                    source_object=PostModel.model_validate(initial_model, from_attributes=True).model_dump(mode="json")
                ))
                session.commit()


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