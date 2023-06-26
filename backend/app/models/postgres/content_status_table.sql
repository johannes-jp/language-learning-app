-- Table: Content Status (For assigning privileges to various forms of content)
CREATE TABLE ContentStatus (
    id SERIAL PRIMARY KEY, -- Unique identifier for each content status
    status TEXT NOT NULL UNIQUE, -- Official, admin-approved, unmoderated, pending-approval, community-favorite, flagged-for-review, etc.
    description TEXT -- Description of the content status
);