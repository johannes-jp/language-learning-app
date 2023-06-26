-- Table: Lists
CREATE TABLE Lists (
    id BIGINT REFERENCES Content(id), -- Unique identifier for each list
    status INT REFERENCES ContentStatus(id), -- Status of the list
    owner_id INT REFERENCES UserCredentials(id), -- User who controls the list
    language_tag VARCHAR(50) REFERENCES Languages(language_tag), -- Language tag that the list pertains to
    name JSONB, -- Key-value pairs where key = language tag, value = name of the list in that language
    description JSONB -- Key-value pairs where key = language tag, value = description of the list in that language
);