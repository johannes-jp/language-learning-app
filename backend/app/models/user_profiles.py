-- Table: User Profiles
CREATE TABLE UserProfiles (
    id INT PRIMARY KEY REFERENCES UserCredentials(id), -- User ID
    username TEXT NOT NULL UNIQUE, -- Username chosen by the user
    reputation INT, -- Measure of user contribution level
    tier ENUM('basic','standard','premium'), -- Paid tiers for feature access
    flair TEXT, -- User title, like admin, professor, student, etc.
    is_private BOOLEAN -- Whether or not user profile is visible to other users
);