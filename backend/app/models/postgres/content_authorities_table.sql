-- Table: Content Authorities (Information sources with elevated content management privileges)
CREATE TABLE ContentAuthorities (
    id SERIAL PRIMARY KEY, -- Unique identifier for each content authority
    organization TEXT NOT NULL UNIQUE, -- Name of the source (Wiktionary, Oxford, etc.)
    authority_link TEXT -- Link to authority homepage, which determines control over any content sourcing to their domain
);