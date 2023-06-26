from backend.app.models import (
    Content,
    ContentAuthorities,
    ContentStatus,
    ContentRelationships,
    ContentRelationshipTypes,
)
from backend.app.services.database import get_db


def create_content(content_data):
    db = get_db()
    new_content = Content(**content_data)
    db.add(new_content)
    db.commit()
    db.refresh(new_content)
    return new_content


def get_content_by_id(content_id):
    db = get_db()
    content = db.query(Content).filter_by(id=content_id).first()
    return content


def update_content(content_id, updated_data):
    db = get_db()
    content = db.query(Content).filter_by(id=content_id).first()
    for key, value in updated_data.items():
        setattr(content, key, value)
    db.commit()
    return content


def delete_content(content_id):
    db = get_db()
    content = db.query(Content).filter_by(id=content_id).first()
    db.delete(content)
    db.commit()
