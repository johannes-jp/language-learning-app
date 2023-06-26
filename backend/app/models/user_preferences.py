-- Table: User Preferences
CREATE TABLE UserPreferences (
    id INT PRIMARY KEY REFERENCES UserCredentials(id), -- Unique identifier for each user
    interface_language VARCHAR(50) REFERENCES Languages(language_tag), -- Language in which the user wants the app interface to be displayed
    base_language VARCHAR(50) REFERENCES Languages(language_tag), -- Language of understanding and regional flavor for translated content
    learning_goals JSONB, -- Daily or weekly goals for the user's learning process
    learning_style TEXT, -- Preferred way of learning for the user, like flashcards, fill-blank, visual, audio, interactive, etc.
    notifications JSONB, -- Preferences for different types of notifications
    privacy_settings JSONB, -- User's preferences related to privacy
    theme ENUM('light', 'dark', 'system'), -- User's preferred theme for the application
    timezone TEXT -- Timezone strings
);