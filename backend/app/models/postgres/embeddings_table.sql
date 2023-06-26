-- Table: Embeddings
CREATE TABLE Embeddings (
    content_id UUID PRIMARY KEY REFERENCES Content(id), -- Unique identifier for each content item
    vector JSONB -- Content embedding vector
);