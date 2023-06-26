-- Table: User Roles (For assigning privileges based on user status)
CREATE TABLE UserRoles (
    id SERIAL PRIMARY KEY, -- Unique identifier for each user role
    name TEXT NOT NULL UNIQUE, -- Admin, teacher, student, etc.
    description TEXT -- Description of the user role
);