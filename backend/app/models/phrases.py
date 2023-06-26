-- Table: Phrases - A phrase is a sequence of content that should have its own relationships. It can have its own media to describe itself, or be constructed by a component list of words/signs.
CREATE TABLE Phrases (
    id BIGINT PRIMARY KEY REFERENCES Content(id), -- Unique identifier for each content sequence
    phrase JSONB, -- The string of the actual sentence, or the URL to the media storing the sequence's self-contained content.
    components ARRAY, -- An ordered list of content_ids that compose the phrase.
    composite BOOLEAN, -- Whether the phrase is self-evident, or constructed from the members of the components array.
    karma INT -- User upvotes and downvotes of phrase accuracy or relevance.
);