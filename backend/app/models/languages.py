from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.dialects.postgresql import JSONB
from .base import Base


class Languages(Base):
    __tablename__ = "languages"

    id = Column(Integer, primary_key=True, autoincrement=True)
    language_tag = Column(String(50), nullable=False, unique=True)
    names = Column(JSONB)
    num_speakers = Column(Integer)


# -- Table: Languages (List of all accepted languages)
# CREATE TABLE Languages (
#     id SERIAL PRIMARY KEY, -- Unique identifier for each language
#     language_tag VARCHAR(50) NOT NULL UNIQUE, -- BCP 47 tag for that language
#     names JSONB, -- Key-value pairs where key = language tag, value = name of the language in that language
#     num_speakers INT -- The estimated number of native speakers of the language
# );
