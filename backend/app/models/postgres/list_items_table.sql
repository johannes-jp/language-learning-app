-- Table: List Items
CREATE TABLE ListItems (
    list_id BIGINT REFERENCES Lists(id), -- The list that the content item belongs to
    content_id BIGINT REFERENCES Content(id), -- The content in the list
    priority INT -- Priority of this content within the list
);