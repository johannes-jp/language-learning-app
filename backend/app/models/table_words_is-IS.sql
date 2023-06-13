CREATE TABLE YourTableName (
    content_id UUID PRIMARY KEY,
    word TEXT NOT NULL,
    language_code CHAR(5) NOT NULL CHECK (language_code = 'is-IS'),
    translation UUID[],
    part_of_speech TEXT,
    word_roots UUID[],
    media_image TEXT,
    media_audio TEXT,
    sentences UUID[]
);