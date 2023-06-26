-- Table: Study History
CREATE TABLE StudyHistory (
    study_id BIGSERIAL PRIMARY KEY, -- Unique identifier for each instance of studied content
    user_id INT REFERENCES UserCredentials(id), -- User who studied the content
    content_id BIGINT REFERENCES Content(id), -- Content that was studied
    relationship_id BIGINT REFERENCES ContentRelationships(id), -- Target of the studied content
    source_language VARCHAR(50) REFERENCES Languages(language_tag), -- Language of the prompt or input
    target_language VARCHAR(50) REFERENCES Languages(language_tag), -- Language of the response or output
    sr_interval INT, -- Spaced repetition interval for content recall
    study_date DATE, -- Date this content was studied
    next_due_date DATE, -- When this content should be studied next, based on sr_interval
    is_private BOOLEAN -- Whether or not learning activity is visible to other users
);