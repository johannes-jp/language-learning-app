-- Table: Content
CREATE TABLE Content (
    id BIGSERIAL PRIMARY KEY, -- Unique identifier for each content item
    type ENUM('word','affix','sign','phrase','list','syllable'), -- Growing list of content types
    status INT REFERENCES ContentStatus(id), -- Status of the content item
    is_private BOOLEAN, -- Whether the content is visible to other users
    language_tag VARCHAR(50) REFERENCES Languages(language_tag), -- Language of the content
    origin ENUM('user','authority','link'), -- Origin of the content (user-generated, from authority, or linked)
    relevance INT -- The number of times this content is studied or referenced
);