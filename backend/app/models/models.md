# proofread & save gpt convos
- 
- **Languages**
	- `id`: `SERIAL PRIMARY KEY` - Numerical identifier for each language.
	- `language_tag`: `VARCHAR(50) NOT NULL UNIQUE` - BCP tag for that language.	
	- `names`: `JSONB` - Key-value pairs where key = language tag, value = name of the language in that language.
	- `num_speakers`: `INT` - The estimated number of native speakers of the language.
    
- **Sources of truth**
	- `id: SERIAL PRIMARY KEY` - Numerical identifier for each source
	- `name: TEXT NOT NULL` - Name of the source (Wiktionary, Urban Dictionary, Admin-approved, User-defined, etc.)
	- `link: TEXT` - Link to source homepage. If user-generated content links to the domain of an accepted source, it can be automatically added to official content tables.
	
- **Content**
	- `content_id`: `BIGSERIAL PRIMARY KEY` - Unique identifier for each content item.
	- `content_type`: `ENUM('word','sentence','list')` - Growing list of content types.
	- `language_tag:VARCHAR(50) REFERENCES languages(language_tag)`
	- `source_of_truth`: `TEXT REFERENCES sources_of_truth(name)` - The resource providing information about this word. Helpful here for differentiating user content.
	
- **Words**
	- `content_id`: `BIGSERIAL PRIMARY KEY REFERENCES content(content_id)` - Unique identifier for each word.
	- `word`: `TEXT` - The actual word, NULL for unspoken languages.
	- `part_of_speech`: `BIGSERIAL REFERENCES words(content_id)` - The grammatical role that word typically plays, given in the form of a UUID reference to another word (that explains the grammatical role in the native language).
	- `lexical_roots`: `BIGSERIAL ARRAY REFERENCES words(content_id)` - The roots of the word, if any.
	- `source_link`: `TEXT` - URL to word's source of truth.
	- `context`: `JSONB` - Flexible additional exposition of the content, like URLs to image/audio/video media, descriptions of sign language movements, etc. 
    
- **Sentences**  
	- `content_id`: `BIGSERIAL PRIMARY KEY REFERENCES content(content_id)` - Unique identifier for each sentence.
	- `sentence`: `TEXT NOT NULL` - The actual sentence.
	- `split`: `ARRAY` - A normalized text list of the words in the sentence.
	- `karma`: `INT` - User upvotes and downvotes of sentence accuracy or relevance.
	
- **Content relationships**
	- `relationship_id`: `BIGSERIAL PRIMARY KEY` - Unique identifier for translation pair.
	- `relationship_type`: `ENUM('translation','definition','synonym','example','category','homonym','list_name','sign_description')` - Growing list of approved relationships.
	- `member1`: `BIGSERIAL REFERENCES content(content_id)`
	- `member2`: `BIGSERIAL REFERENCES content(content_id)`
	- `accuracy`: `FLOAT` - How accurately the two members represent one another.
	
- **Learning lists**
    - `list_id`: `SERIAL PRIMARY KEY` - Unique identifier for each learning list.
    - `status`: `ENUM('official','approved','unapproved')` - List created by admins, approved by admins, or unmoderated.
    - `user_id`: `INT REFERENCES user_profile(user_id)` - Who owns this list, if it is user-managed.
    - `language_tag`: `VARCHAR(50)` - The language tag that this list pertains to.
    - `name`: `JSONB` - Key-value pairs where key = language tag, value = name of the list in that language.
    - `description`: `JSONB` - Key-value pairs where key = language tag, value = description of the list in that language.
    - `is_private`: `BOOLEAN` Whether or not the list is visible to other users.
	
- **Learning list items**
	- `PRIMARY KEY (list_id, content_id)`
	- `list_id`: `INT PRIMARY KEY REFERENCES learning_lists(list_id)` - The list this content item belongs to.
	- `content_id`: `BIGSERIAL REFERENCES content(content_id)` - Reference to content in either words or sentences table.
	- `priority`: `INT` - Priority of this content within the list.
	
- **User credentials**
	- `user_id`: `SERIAL PRIMARY KEY` - Unique identifier for each user.
	- `email`: `TEXT NOT NULL UNIQUE` - Email address of the user.
	- `hashed_password`: `TEXT NOT NULL` - Hashed password for user login.
	
- **User info**
	- `user_id`: `INT PRIMARY KEY REFERENCES user_credentials(user_id)`
	- `name`: `TEXT NOT NULL UNIQUE` - Username chosen by the user.
	- `reputation`: `INT` - Measure of user's contribution level. 
	- `tier`: `ENUM('basic','standard','premium')`
	- `flair`: `TEXT` - User's title, like admin, professor, student, etc.
	
- **User Preferences**
	- `user_id`: `INT PRIMARY KEY REFERENCES user_profile(user_id) PRIMARY KEY` - The unique identifier of the user these preferences belong to.
	- `interface_language`: `VARCHAR(50) REFERENCES languages(language_tag)` - The language in which the user wants the app interface to be displayed.
	- `base_language`: `VARCHAR(50) REFERENCES languages(language_tag)` - The base language and regional flavor for translated content. 
	- `learning_goals`: `JSONB` - The daily or weekly goals for the user's learning process.
	- `notifications`: `JSONB` - Preferences for different types of notifications, such as email notifications, push notifications, daily reminders, etc.
	- `privacy_settings`: `JSONB` - The user's preferences related to privacy like showing their profile to others, sharing progress with others etc.
	- `learning_style`: `TEXT` - The preferred way of learning for the user, like visual, audio, interactive, etc.
	- `theme`: `ENUM('light', 'dark', 'system')` - The user's preferred theme for the application.
	- `timezone`: `INT` - The user's time zone in +/- UTC.
	- `pronunciation_accent`: `TEXT` - For a language learning app, users might prefer learning pronunciation in a certain accent.
	
- **User study history** - all instances of studied content
	- `study_id`: `BIGSERIAL PRIMARY KEY`
	- `user_id`: `INT REFERENCES user_profile(user_id)` - The user who studied the content.
	- `content_id`: `BIGINT REFERENCES content(content_id)` - The content that was studied.
	- `source_language`: `VARCHAR(50) REFERENCES content(language_tag)` - Static reference to content language.
	- `target_language`: `VARCHAR(50)` - Static reference to the user's language of understanding. Selects from user preferences by default. 
	- `sr_interval`: `INT` - Spaced repetition interval for content recall. Note that reversing target & source is the difference between reading and speaking.
	- `study_date`: `DATE` - The date this content was studied. Serial `study_id` allows for multiple reviews per day.
	- `next_due_date`: `DATE` - When this content should be studied next, based on `sr_interval`.
	
- **Embeddings**
    
    - `content_id`: `UUID PRIMARY KEY` - Unique identifier for each content.
    - `vector`: `JSONB` - Word or sentence embedding vector.
