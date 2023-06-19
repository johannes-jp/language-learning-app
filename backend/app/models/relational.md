### with postgres

- **Languages** - List of all accepted languages.
	- `id`: `SERIAL PRIMARY KEY`
	- `language_tag`: `VARCHAR(50) NOT NULL UNIQUE` - BCP tag for that language.	
	- `names`: `JSONB` - Key-value pairs where key = language tag, value = name of the language in that language.
	- `num_speakers`: `INT` - The estimated number of native speakers of the language.
    
- **Content Authorities** - Information sources with elevated content management privileges. 
	- `id`: `SERIAL PRIMARY KEY`
	- `organization`: `TEXT NOT NULL UNIQUE` - Name of the source (Wiktionary, Oxford, etc.)
	- `authority_link`: `TEXT` - Link to authority homepage, which determines control over any content sourcing to their domain.  
	
- **User roles** - For assigning privileges based on user status.
	- `id`: `SERIAL PRIMARY KEY`
	- `name`: `TEXT NOT NULL UNIQUE` - Admin, teacher, student, etc.
	- `description`: `TEXT`
	
- **Content status** - For assigning privileges to various forms of content.
	- `id`: `SERIAL PRIMARY KEY`
	- `status`: `TEXT NOT NULL UNIQUE` - Official, admin-approved, unmoderated, pending-approval, community-favorite, flagged-for-review, etc. 
	- `description`: `TEXT`
	
- **Relationship types** - Catalog of the large variety of contextual relationships that can exist.
	- `id`: `SERIAL PRIMARY KEY`
	- `type`: `TEXT` - Translation, definition, synonym, example, lexical_root, part_of_speech, category, homonym, sign_description, list_name, etc.
	- `description`: `TEXT`
	
- **Content**
	- `id`: `BIGSERIAL PRIMARY KEY` - Unique identifier for each content item.
	- `type`: `ENUM('word','sign','phrase','list')` - Growing list of content types.
	- `status`: `INT REFERENCES content_status(id)`
	- `is_private`: `BOOLEAN` - Whether the content is visible to other users.
	- `language_tag:VARCHAR(50) REFERENCES languages(language_tag)`.
	- `origin`: 
	- `ENUM('user','authority','link')`
	- `relevance`: `INT` - The number of times this content is studied or referenced.
	
- **Words** - Frequently referenced relationships for . 
	- `id`: `BIGINT PRIMARY KEY REFERENCES content(id)`
	- `word`: `TEXT` - The actual word.
	- `source_of_truth`: `TEXT` - URL to word's source of truth.
	- `context`: `JSONB` - Flexible additional exposition of the content, like URLs to image/audio/video media, etc. 
	
- **Signs**
	- `content_id`: `BIGSERIAL PRIMARY KEY REFERENCES content(id)` - Unique identifier for visual communications.
	- `type`: `ENUM('sign_language','street_sign','image','gesture','facial_expression','tactile_language')` - Type of the sign.
	- `sign_data`: `JSONB` - Data representing the sign, image, gesture, etc. Could include links to media files, arrays for tactile languages, and other relevant data.
	- `context`: `JSONB` - Flexible additional information about the sign, such as the cultural context, location where it's used, etc.
	
- **Phrases**  
	- `id`: `BIGINT PRIMARY KEY REFERENCES content(id)` - Unique identifier for each content sequence.
	- `sentence`: `TEXT NOT NULL` - The actual sentence.
	- `split_words`: `ARRAY` - A normalized text list of the words in the sentence.
	- `karma`: `INT` - User upvotes and downvotes of sentence accuracy or relevance.
	

- **Content relationships**
	- `id`: `BIGSERIAL PRIMARY KEY`
	- `originator`: `BIGINT REFERENCES user_credentials(id)`
	- `relationship_type`: `TEXT REFERENCES relationship_types(id)`- Definition, synonym, etc.
	- `member1`: `BIGINT REFERENCES content(id)` - First node for relationship link. In hierarchical relationships this is the parent, likely the source language.
	- `member2`: `BIGINT REFERENCES content(id)` - Second node for relationship link. In hierarchical relationships this is the child, likely the target language.
	- `source_of_truth`: `TEXT` - URL to the source that justifies this relationship.
	- `confidence`: `FLOAT CHECK (confidence >=0 AND confidence <=1)` - How accurately the two members represent one another.
	- `status`: `INT REFERENCES content_status(id)` - 
	- `karma`: `INT` - User upvotes and downvotes of entity quality.
	- `relevance`: `INT` - The number of times this content is studied or referenced.
	
- **Lists**
    - `id`: `BIGINT REFERENCES content(id)`
    - `status`: `INT REFERENCES content_status(id)` - List created by admins, approved by admins, or unmoderated.
    - `owner_id`: `INT REFERENCES user_credentials(id)` - Who controls this list. Admin and system profiles used for 'official' lists.
    - `language_tag`: `VARCHAR(50) REFERENCES languages(language_tag)` - The language tag that this list pertains to.
    - `name`: `JSONB` - Key-value pairs where key = language tag, value = name of the list in that language.
    - `description`: `JSONB` - Key-value pairs where key = language tag, value = description of the list in that language.
	
- **List items**
	- `PRIMARY KEY (list_id, content_id)`
	- `list_id`: `BIGINT PRIMARY KEY REFERENCES lists(id)` - The list this content item belongs to.
	- `content_id`: `BIGINT REFERENCES content(id)` - The content in the list.
	- `priority`: `INT` - Priority of this content within the list.
	
- **User Credentials**
	- `id`: `SERIAL PRIMARY KEY` - Unique identifier for each user.
	- `email`: `TEXT NOT NULL UNIQUE` - Email address of the user.
	- `hashed_password`: `TEXT NOT NULL` - Hashed password for user login.
	- `account`: `ENUM('active','disabled')` - Whether the account is functional or not.
	
- **User Profiles**
	- `id`: `INT PRIMARY KEY REFERENCES user_credentials(id)` - User ID.
	- `username`: `TEXT NOT NULL UNIQUE` - Username chosen by the user.
	- `reputation`: `INT` - Measure of user contribution level. 
	- `tier`: `ENUM('basic','standard','premium')` - Paid tiers for feature access.
	- `flair`: `TEXT` - User title, like admin, professor, student, etc.
	- `is_private`: `BOOLEAN` - Whether or not user profile is visible to other users.
	
- **User Preferences**
	- `id`: `INT PRIMARY KEY REFERENCES user_credentials(id) PRIMARY KEY` - The unique identifier of the user these preferences belong to.
	- `interface_language`: `VARCHAR(50) REFERENCES languages(language_tag)` - The language in which the user wants the app interface to be displayed.
	- `base_language`: `VARCHAR(50) REFERENCES languages(language_tag)` - The language of understanding and regional flavor for translated content. 
	- `learning_goals`: `JSONB` - The daily or weekly goals for the user's learning process.
	- `learning_style`: `TEXT` - The preferred way of learning for the user, like flashcards, fill-blank, visual, audio, interactive, etc.
	- `notifications`: `JSONB` - Preferences for different types of notifications, such as email notifications, push notifications, daily reminders, etc.
	- `privacy_settings`: `JSONB` - The user's preferences related to privacy like showing their profile to others, sharing progress with others, sharing lists, etc.
	- `theme`: `ENUM('light', 'dark', 'system')` - The user's preferred theme for the application.
	- `timezone`: `TEXT` - Timezone strings.
	
- **Study history**
	- `study_id`: `BIGSERIAL PRIMARY KEY` - Unique identifier for each instance of studied content.
	- `user_id`: `INT REFERENCES user_credentials(id)` - The user who studied the content.
	- `content_id`: `BIGINT REFERENCES content(id)` - The content that was studied.
	- `relationship_id`: `BIGINT REFERENCES content_relationships(id)` - The target of that studied content.
	- `source_language`: `VARCHAR(50) REFERENCES languages(language_tag)` - Language of the prompt or input.
	- `target_language`: `VARCHAR(50) REFERENCES languages(language_tag)` - Language of the response or output.
	- `sr_interval`: `INT` - Spaced repetition interval for content recall. Note that reversing target & source is the difference between reading and speaking.
	- `study_date`: `DATE` - The date this content was studied. Serial `study_id` allows for multiple reviews per day.
	- `next_due_date`: `DATE` - When this content should be studied next, based on `sr_interval`.
	- `is_private`: `BOOLEAN` - Whether or not learning activity is visible to other users.
	
- **Embeddings**
    - `content_id`: `UUID PRIMARY KEY REFERENCES content(id)` - Unique identifier for each content item.
    - `vector`: `JSONB` - Word or sentence embedding vector.
