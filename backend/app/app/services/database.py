from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from .models import Base

DATABASE_URL = "postgresql://user:password@localhost:5432/mydatabase"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def execute_query(query, *args, **kwargs):
    try:
        with SessionLocal() as session:
            session.execute(query, *args, **kwargs)
            session.commit()
    except SQLAlchemyError as e:
        session.rollback()
        raise e


def add_object(obj):
    try:
        with SessionLocal() as session:
            session.add(obj)
            session.commit()
    except SQLAlchemyError as e:
        session.rollback()
        raise e


def delete_object(obj):
    try:
        with SessionLocal() as session:
            session.delete(obj)
            session.commit()
    except SQLAlchemyError as e:
        session.rollback()
        raise e


def get_objects(model):
    try:
        with SessionLocal() as session:
            return session.query(model).all()
    except SQLAlchemyError as e:
        session.rollback()
        raise e
