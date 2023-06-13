CREATE TABLE words (
    content_id UUID PRIMARY KEY,
    word TEXT NOT NULL,
    language_code CHAR(5) NOT NULL,
    simple_translation JSONB,
    part_of_speech TEXT,
    lexical_roots UUID[],
    definition JSONB,
    media_image TEXT,
    media_audio TEXT,
    sentences UUID[]
);