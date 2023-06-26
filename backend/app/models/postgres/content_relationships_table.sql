-- Table: Content Relationships
CREATE TABLE ContentRelationships (
    id BIGSERIAL PRIMARY KEY, -- Unique identifier for each content relationship
    originator BIGINT REFERENCES UserCredentials(id), -- User who created the relationship
    relationship_type TEXT REFERENCES RelationshipTypes(id), -- Type of the relationship
    member1 BIGINT REFERENCES Content(id), -- First node for relationship link
    member2 BIGINT REFERENCES Content(id), -- Second node for relationship link
    source_of_truth TEXT, -- URL to the source that justifies this relationship
    confidence FLOAT CHECK (confidence >=0 AND confidence <=1), -- How accurately the two members represent one another
    status INT REFERENCES ContentStatus(id), -- Status of the relationship
    karma INT, -- User upvotes and downvotes of entity quality
    relevance INT -- The number of times this content is studied or referenced
);