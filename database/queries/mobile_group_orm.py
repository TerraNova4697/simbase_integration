# from sqlalchemy import select
# from sqlalchemy.exc import IntegrityError

# from database.models import MobileGroup
# from database.superset_models import MobGroup as SsMobGroup, SqlError
# from database.simbase_database import session_factory
# from database.superset_database import superset_session_factory
# from logger import logger
# from helper_models import MobGroupModel

# from traceback import format_exc


# class SsMobGroupOrm:

#     @staticmethod
#     def create(**kwargs) -> None:
#         with superset_session_factory() as session:
#             initial_model = kwargs.pop("model")
#             try:
#                 mob_group = SsMobGroup(**kwargs)
#                 session.add(mob_group)
#                 session.commit()
#             except IntegrityError as exc:
#                 session.rollback()
#                 compiled = mob_group.__table__.insert().values(**kwargs).compile(compile_kwargs={"literal_binds": True})
#                 session.add(SqlError(
#                     exception=str(exc.__class__),
#                     traceback=format_exc(),
#                     sql=str(compiled),
#                     target_model=SsMobGroup.__name__,
#                     source_object=MobGroupModel.model_validate(initial_model, from_attributes=True).model_dump(mode="json")
#                 ))
#                 session.commit()


# class MobileGroupOrm:

#     @staticmethod
#     def all(**kwargs):
#         with session_factory() as session:
#             query = select(MobileGroup)
#             if kwargs.get('date'):
#                 query.where(MobileGroup.date)
#             return session.execute(query).scalars().all()

#     @staticmethod
#     def insert(**kwargs):
#         with session_factory() as session:
#             obj = MobileGroup(**kwargs)
#             session.add(obj)
#             session.commit()
