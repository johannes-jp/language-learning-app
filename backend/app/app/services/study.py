from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from .models import StudyHistory
from .database_service import execute_query, add_object, get_objects, delete_object


def get_study_history_by_user_id(db: Session, user_id: int):
    try:
        return db.query(StudyHistory).filter(StudyHistory.user_id == user_id).all()
    except SQLAlchemyError as e:
        raise e


def create_study_history(db: Session, study_history: StudyHistory):
    try:
        add_object(study_history)
    except SQLAlchemyError as e:
        raise e


def update_study_history(db: Session, study_history: StudyHistory):
    try:
        db.query(StudyHistory).filter(StudyHistory.id == study_history.id).update(
            {
                StudyHistory.study_time: study_history.study_time,
                StudyHistory.language_id: study_history.language_id,
                StudyHistory.user_id: study_history.user_id,
            }
        )
        db.commit()
    except SQLAlchemyError as e:
        db.rollback()
        raise e


def delete_study_history(db: Session, study_history_id: int):
    try:
        study_history = (
            db.query(StudyHistory).filter(StudyHistory.id == study_history_id).one()
        )
        delete_object(study_history)
    except SQLAlchemyError as e:
        raise e
