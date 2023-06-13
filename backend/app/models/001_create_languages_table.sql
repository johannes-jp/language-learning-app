CREATE TABLE Languages (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    num_speakers INTEGER,
    language_code CHAR(5) NOT NULL UNIQUE
);
