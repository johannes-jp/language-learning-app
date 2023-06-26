from sqlalchemy import Column, Integer, ForeignKey
from .base import Base


class ListItems(Base):
    __tablename__ = "listitems"

    list_id = Column(Integer, ForeignKey("lists.id"), primary_key=True)
    content_id = Column(Integer, ForeignKey("content.id"), primary_key=True)
    priority = Column(Integer)


# -- Table: List Items
# CREATE TABLE ListItems (
#     list_id BIGINT REFERENCES Lists(id), -- The list that the content item belongs to
#     content_id BIGINT REFERENCES Content(id), -- The content in the list
#     priority INT -- Priority of this content within the list
# );
