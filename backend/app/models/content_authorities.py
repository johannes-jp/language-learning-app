from sqlalchemy import Column, Integer, String
from .base import Base


class ContentAuthorities(Base):
    __tablename__ = "content_authorities"

    id = Column(Integer, primary_key=True, index=True)
    organization = Column(String, unique=True, nullable=False)
    user_id = 
    authority_link = Column(String)


# -- Table: Content Authorities (Information sources with elevated content management privileges)
# CREATE TABLE ContentAuthorities (
#     id SERIAL PRIMARY KEY, -- Unique identifier for each content authority
#     organization TEXT NOT NULL UNIQUE, -- Name of the source (Wiktionary, Oxford, etc.)
#     authority_link TEXT -- Link to authority homepage, which determines control over any content sourcing to their domain
