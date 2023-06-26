-- Table: Words - All morphemes go here. Usually lexemes (words), but subcomponents like suffixes and syllables are welcome here too.
CREATE TABLE Words (
    id BIGINT PRIMARY KEY REFERENCES Content(id), -- Unique identifier for each word
    word TEXT, -- The actual word
    language_tag VARCHAR(50), -- Language the word belongs to
    source_of_truth TEXT, -- URL to word's source of truth
    context JSONB -- Flexible additional exposition of the content, like URLs to image/audio/video media, etc.
);