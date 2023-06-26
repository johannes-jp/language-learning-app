from flask import g
from werkzeug.security import generate_password_hash, check_password_hash
from backend.app.models import UserCredentials, UserProfiles, UserRoles
from backend.app.services.database import get_db


def register_user(username, password):
    if username is None or password is None:
        raise ValueError("Username and Password must not be None.")

    db = get_db()
    existing_user = db.query(UserCredentials).filter_by(username=username).first()
    if existing_user is not None:
        raise ValueError("Username already exists.")

    password_hash = generate_password_hash(password)
    new_user = UserCredentials(username=username, password_hash=password_hash)

    db.add(new_user)
    db.commit()

    return new_user


def authenticate_user(username, password):
    db = get_db()
    user = db.query(UserCredentials).filter_by(username=username).first()

    if user is None or not check_password_hash(user.password_hash, password):
        return None

    return user


def change_password(user_id, new_password):
    db = get_db()
    user = db.query(UserCredentials).filter_by(id=user_id).first()

    if user is None:
        raise ValueError("Invalid user id.")

    user.password_hash = generate_password_hash(new_password)
    db.commit()

    return user


def get_user_profile(user_id):
    db = get_db()
    user_profile = db.query(UserProfiles).filter_by(user_id=user_id).first()

    return user_profile


def get_user_role(user_id):
    db = get_db()
    user_role = db.query(UserRoles).filter_by(user_id=user_id).first()

    return user_role
