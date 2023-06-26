-- Table: User Credentials
CREATE TABLE UserCredentials (
    id SERIAL PRIMARY KEY, -- Unique identifier for each user
    email TEXT NOT NULL UNIQUE, -- Email address of the user
    hashed_password TEXT NOT NULL, -- Hashed password for user login
    account ENUM('active','disabled') -- Whether the account is functional or not
);