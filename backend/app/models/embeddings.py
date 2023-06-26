from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID, JSONB
from .base import Base


class Embeddings(Base):
    __tablename__ = "embeddings"

    content_id = Column(UUID(as_uuid=True), ForeignKey("content.id"), primary_key=True)
    vector = Column(JSONB)


# -- Table: Embeddings
# CREATE TABLE Embeddings (
#     content_id UUID PRIMARY KEY REFERENCES Content(id), -- Unique identifier for each content item
#     vector JSONB -- Content embedding vector
# );
