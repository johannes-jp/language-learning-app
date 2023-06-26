from sqlalchemy import Column, Integer, Boolean, Enum, ForeignKey, String
from sqlalchemy.dialects.postgresql import BIGINT
from .base import Base
import enum


class ContentTypeEnum(enum.Enum):
    word = "word"
    affix = "affix"
    sign = "sign"
    phrase = "phrase"
    list = "list"
    syllable = "syllable"


class ContentStatusEnum(enum.Enum):
    OFFICIAL = "Official"
    ADMIN_APPROVED = "admin-approved"
    UNMODERATED = "unmoderated"
    PENDING_APPROVAL = "pending-approval"
    COMMUNITY_FAVORITE = "community-favorite"
    FLAGGED_FOR_REVIEW = "flagged-for-review"


class Content(Base):
    __tablename__ = "Content"

    id = Column(BIGINT, primary_key=True, index=True)
    type = Column(Enum(ContentTypeEnum))
    status = Column(Enum(ContentStatusEnum), nullable=False)
    is_private = Column(Boolean)
    originator = Column(Integer, ForeignKey("UserCredentials.id"))
    popularity = Column(Integer)


# -- Table: Content
# CREATE TABLE Content (
#     id BIGSERIAL PRIMARY KEY, -- Unique identifier for each content item
#     type ENUM('word','affix','sign','phrase','list','syllable'), -- Growing list of content types
#     status INT REFERENCES ContentStatus(id), -- Status of the content item
#     is_private BOOLEAN, -- Whether the content is visible to other users
#     language_tag VARCHAR(50) REFERENCES Languages(language_tag), -- Language of the content
#     origin ENUM('user','authority','link'), -- Origin of the content (user-generated, from authority, or linked)
#     relevance INT -- The number of times this content is studied or referenced
# );
