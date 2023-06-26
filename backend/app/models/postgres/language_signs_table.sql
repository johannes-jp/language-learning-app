-- Table: Signs - A sign is anything that can't be 
CREATE TABLE Signs ( -- anything that can't be 
    content_id BIGSERIAL PRIMARY KEY REFERENCES Content(id), -- Unique identifier for visual communications
    type ENUM('sign_language','street_sign','image','gesture','facial_expression','tactile_language'), -- Type of the sign
    sign_data JSONB, -- Data representing the sign, image, gesture, etc.
    context JSONB -- Flexible additional information about the sign, such as the cultural context, location where it's used, etc.
);