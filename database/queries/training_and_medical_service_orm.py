from sqlalchemy import select

from database.models import TrainingAndMedicalService
from database.superset_models import TrainingAndMedicalService as SsTrainingAndMedicalService
from database.simbase_database import session_factory
from database.queries.base_orm import BaseOrm


class SsTrainingAndMedicalServiceOrm(BaseOrm):
    target_model = SsTrainingAndMedicalService


class TrainingAndMedicalServiceOrm:

    @staticmethod
    def all(**kwargs) -> list[TrainingAndMedicalService]:
        with session_factory() as session:
            query = (
                select(
                    TrainingAndMedicalService
                )
            )
            if kwargs.get('date'):
                query.where(TrainingAndMedicalService.date == kwargs['date'])
            return session.execute(query).scalars().all()