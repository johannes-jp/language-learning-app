-- Table: Relationship Types (Catalog of the large variety of contextual relationships that can exist)
CREATE TABLE RelationshipTypes (
    id SERIAL PRIMARY KEY, -- Unique identifier for each relationship type
    type TEXT, -- Translation, definition, synonym, example, lexical_root, part_of_speech, category, homonym, sign_description, list_name, etc.
    description TEXT -- Description of the relationship type
);