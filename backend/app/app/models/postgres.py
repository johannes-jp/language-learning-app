from sqlalchemy import Column, Integer, Boolean, Enum, ForeignKey, String, JSON
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import BIGINT, UUID, JSONB

from .base import Base
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from typing import TYPE_CHECKING

from app.db.base_class import Base

if TYPE_CHECKING:
    from .item import Item  # noqa: F401


# Reference Tables

class Languages(Base):
    __tablename__ = "languages"
    '''
    - **Languages** - List of all accepted languages.
        - `id`: `SERIAL PRIMARY KEY`
        - `language_tag`: `VARCHAR(50) NOT NULL UNIQUE` - BCP tag for that language.	
        - `names`: `JSONB` - Key-value pairs where key = language tag, value = name of the language in that language.
        - `num_speakers`: `INT` - The estimated number of native speakers of the language.
        - `grammar`: `ARRAY REFERENCE grammar_elements(id)` - List of grammar ids that the language uses.
    '''
    id = Column(Integer, primary_key=True, autoincrement=True)
    language_tag = Column(String(50), nullable=False, unique=True)
    names = Column(JSONB)
    num_speakers = Column(Integer)
    grammar: ARRAY REFERENCE grammar_elements(id)

class GrammarElements(Base):
    '''
    - **Grammar Elements**
        - id: serial primary key
        - name: All types, tenses, moods, etc. 
        - `fst`: - Dict of finite state transducer codes with their language id
    '''
    __tablename__ = "grammar_elements"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    fst = finite state transducer codes in various languages

    # reverse relationship
    languages = relationship("Languages", secondary=grammar_association_table)

class RelationshipTypes(Base):
    """
    - **Relationship Types** - Catalog of the large variety of contextual relationships that can exist. Keep in mind relational syntax for wikiData, etc.
        - `id`: `SERIAL PRIMARY KEY`
        - `type`: `TEXT` - Translation, definition, synonym, example, lexical_root, part_of_speech, category, homonym, synonym, hyponym, hypernym,  sign_description, list_name, media_representation, numerical_representation, link, cultural_context, etc.
        - `description`: `TEXT`
    """

class ContentAuthorities(Base):
    '''
    - **Content Authorities** - Information sources with elevated content management privileges. 
        - `id`: `SERIAL PRIMARY KEY`
        - `organization`: `TEXT NOT NULL UNIQUE` - Name of the source (Wiktionary, Oxford, etc.)
        - `user_id`: `INT REFERENCES user_profiles(id)` Reference to user ID
        - `authority_link`: `TEXT` - Link to authority homepage, which determines control over any content sourcing to their domain.
    '''
    __tablename__ = "content_authorities"

    id = Column(Integer, primary_key=True, index=True)
    organization = Column(String, unique=True, nullable=False)
    user_id = 
    authority_link = Column(String)

class WikidataEntities(Base):
    __tablename__ = ""
    '''
    - entities
      - wikidata property (Q18616576)
        - type of wikidata property (Q107649491)
          - wikidata property for items about languages (Q20824104)
      - Specific language (Q1412)
        - number of speakers, writers, or signers (P1098)
        - Icelandic (Q294)
        - Finnish (Q1412)
        - English
    - properties 
      - grammar
        - has typology (P4132)
        - has case (P2989)
        - has tense (P3103)
        - has mood (P3161)
        - has gender (P5109)
        - has person (P5110)
    '''

# Contentful Tables

class Content(Base):
    """
    - **Content** - Mgmt metadata for all content types. Consider splitting into lexographical and meta-content tables.
        - `id`: `BIGSERIAL PRIMARY KEY` - Unique identifier for each content item.
        - `type`: `INT REFERENCE content_types(id)`
        - `status`: `ENUM('official','admin_approved','unmoderated','pending_approval','community_favorite','flagged_for_review')` - For assigning content privileges. If too many categories, may be split into its own table:
            -  **Content Statuses** - For assigning privileges to various forms of content.
                - `id`: `SERIAL PRIMARY KEY`
                - `status`: `TEXT NOT NULL UNIQUE` - Official, admin-approved, unmoderated, pending-approval, community-favorite, flagged-for-review, sponsored, etc.
                - `description`: `TEXT`
        - `type`: `ENUM('word','affix','fragment','sign','phrase','list','syllable')` - If too many categories, may be split into its own table:
            - **Content Types**
                - `id`: `SERIAL PRIMARY KEY`
                - `type`: `TEXT NOT NULL UNIQUE` - Word, affix, sign, phrase, syllable, list, video, image, audio, lexeme, morpheme, etc.
                - `format`: `ENUM('text','image','video','audio')`
                - `description`: `TEXT`
        - `is_private`: `BOOLEAN` - Whether the content is visible to other users.
        - `originator`: `INT REFERENCE user_profiles(id)` - Who made this. Content status determines editing privileges.
        - `popularity`: `INT` - Number of times this content has been accessed.
        - `karma`: `INT` - Might be redundant with popularity, but gives user control to content relevance.
    """

    __tablename__ = "Content"

    id = Column(BIGINT, primary_key=True, index=True)
    type = Column(Enum(ContentTypeEnum))
    status = Column(Enum(ContentStatusEnum), nullable=False)
    is_private = Column(Boolean)
    originator = Column(Integer, ForeignKey("UserCredentials.id"))
    popularity = Column(Integer)

class Words(Base):
    """
    - **Words** - Atomic, mostly indivisible language units (morphemes) of the written and spoken variety. 
        - `id`: `BIGINT PRIMARY KEY REFERENCES content(id)` - Ref to content ID.
        - `word`: `TEXT` - The actual word.
        - `type`: `ENUM('word','affix','syllable','lexeme','stem','morpheme(catch all)'` - Words includes word fragments. Pedantically this table could be called 'atoms' instead of words.
        - `language_tag`: `INT REFERENCE languages(id)` - Ref to language ID
        - `part_of_speech`: `ENUM('noun','verb',etc.)` - Separate from other grammar because it's so distinguishing.
        - `grammar`: `JSONB` - Part of speech, tense, mood, case, etc. #TODO - port to grammar element table.
        - `sources_of_truth`: `JSONB` - Key, value pair of name: reference, like authoritative userID: website.
        - `context`: `JSONB` - Catchall for additional data. Anything in here might deserve its own field. 
    """

class Signs(Base):
    """
    - **Signs** - Atomic, mostly indivisible language units of the visual variety.
        - `id`: `BIGSERIAL PRIMARY KEY REFERENCES content(id)`
        - `type`: `ENUM('sign_language','street_sign','image','gesture','facial_expression','tactile_language')` - Type of the sign.
        - `sign_data`: `JSONB` - Data representing the sign, image, gesture, etc. Could include links to media files, arrays mapping braille characters, and other relevant data.
        - `context`: `JSONB` - Flexible additional information about the sign, such as the cultural context, location where it's used, etc.
    """

class Phrases(Base):
    """
    - **Phrases**  - A phrase is any non-atomic sequence with its own context, which therefore needs its own relationships. It can be self-evident or constructed by a component list of words/signs.
        - `id`: `BIGINT PRIMARY KEY REFERENCES content(id)` - Unique identifier for each content sequence.
        - `phrase`: `JSONB` - The string of the actual phrase, or the URL to the media storing the sequence's self-contained content.
        - `type`: `ENUM('sentence','phrase','compound_word','idiom')` - Falling into relationship territory.
        - `components`: `ARRAY` -- An ordered list of content_ids that compose the phrase.
        - `icing`: `ARRAY` -- Map of extraneous bits like spaces & commas, so the phrase's exact string could be reconstructed when combined with the component array.
        - `composite`: `BOOLEAN` -- Whether the phrase entered the database AS IS, or was constructed from the members of its component array.
    """

class Relationships(Base):
    """
    - **Content relationships**
        - `id`: `BIGSERIAL PRIMARY KEY`
        - `originator`: `INT REFERENCES user_profiles(id)`
        - `relationship_type`: `TEXT REFERENCES relationship_types(id)`- Definition, synonym, etc.
        - `member1`: `BIGINT REFERENCES content(id)` - First node for relationship link. In hierarchical relationships this is the parent, likely the source language.
        - `member2`: `BIGINT REFERENCES content(id)` - Second node for relationship link. In hierarchical relationships this is the child, likely the target language.
        - `source_of_truth`: `TEXT` - URL to the source that justifies this relationship.
        - `confidence`: `FLOAT CHECK (confidence >=0 AND confidence <=1)` - How accurately the two members represent one another.
        - `status`: `INT REFERENCES content_status(id)` - 
        - `karma`: `INT` - User upvotes and downvotes of entity quality.
        - `popularity`: `INT` - The number of times this content is studied or referenced.
    """

class Lists(Base):
    __tablename__ = "lists"
    """
    - **Lists**
        - `id`: `BIGINT REFERENCES content(id)`
        - `name`: `JSONB` - Key-value pairs where key = language tag, value = name of the list in that language.
        - `description`: `JSONB` - Key-value pairs where key = language tag, value = description of the list in that language.
    """
    id = Column(Integer, ForeignKey("content.id"), primary_key=True)
    name = Column(JSON)
    description = Column(JSON)

class ListItems(Base):
    __tablename__ = "listitems"
    """
    - **List items**
        - `PRIMARY KEY (list_id, content_id)`
        - `list_id`: `BIGINT PRIMARY KEY REFERENCES lists(id)` - The list this content item belongs to.
        - `content_id`: `BIGINT REFERENCES content(id)` - The content in the list.
        - `priority`: `INT` - Priority of this content within the list.
    """
    list_id = Column(Integer, ForeignKey("lists.id"), primary_key=True)
    content_id = Column(Integer, ForeignKey("content.id"), primary_key=True)
    priority = Column(Integer)

class StudyHistory(Base):
    """
    - **Study history**
        - `study_id`: `BIGSERIAL PRIMARY KEY` - Unique identifier for each instance of studied content.
        - `user_id`: `INT REFERENCES user_profiles(id)` - The user who studied the content.
        - `content_id`: `BIGINT REFERENCES content(id)` - The content that was studied.
        - `relationship_id`: `BIGINT REFERENCES content_relationships(id)` - The target of that studied content.
        - `source_language`: `VARCHAR(50) REFERENCES languages(language_tag)` - Language of the prompt or input.
        - `target_language`: `VARCHAR(50) REFERENCES languages(language_tag)` - Language of the response or output.
        - `sr_interval`: `INT` - Spaced repetition interval for content recall. Note that reversing target & source is the difference between reading and speaking.
        - `study_date`: `DATE` - The date this content was studied. Serial `study_id` allows for multiple reviews per day.
        - `next_due_date`: `DATE` - When this content should be studied next, based on `sr_interval`.
        - `is_private`: `BOOLEAN` - Whether or not learning activity is visible to other users.
    """


# User Tables

class UserCredentials(Base):
    """
    - **User Credentials**
        - `id`: `INT PRIMARY KEY REFERENCES user_profiles(id)` - Reference to user ID.
        - `email`: `TEXT NOT NULL UNIQUE` - Email address of the user.
        - `hashed_password`: `TEXT NOT NULL` - Hashed password for user login.
    """
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)
    items = relationship("Item", back_populates="owner")

class UserPreferences(Base):
    """
    - **User Preferences**
        - `id`: `INT PRIMARY KEY REFERENCES user_profiles(id) PRIMARY KEY` - Reference to user ID.
        - `interface_language`: `VARCHAR(50) REFERENCES languages(language_tag)` - The language in which the user wants the app interface to be displayed.
        - `base_language`: `VARCHAR(50) REFERENCES languages(language_tag)` - The default language of understanding and regional flavor for translated content. 
        - `learning_goals`: `JSONB` - The daily or weekly goals for the user's learning process.
        - `learning_style`: `TEXT` - The preferred way of learning for the user, like flashcards, fill-blank, visual, audio, interactive, etc.
        - `notifications`: `JSONB` - Preferences for different types of notifications, such as email notifications, push notifications, daily reminders, etc.
        - `privacy_settings`: `JSONB` - The user's preferences related to privacy like showing their profile to others, sharing progress with others, sharing lists, etc.
        - `theme`: `ENUM('light', 'dark', 'system')` - The user's preferred theme for the application.
        - `timezone`: `TEXT` - Timezone strings.
    """

class UserProfiles(Base):
    """
    - **User Profiles**
        - `id`: `SERIAL PRIMARY KEY` - Unique identifier for each user.
        - `username`: `TEXT NOT NULL UNIQUE` - Username chosen by the user.
        - `reputation`: `INT` - Measure of user contribution level. 
        - `tier`: `ENUM('basic','standard','premium')` - Paid tiers for feature access.
        - `flair`: `TEXT` - User title, like admin, professor, student, etc.
        - `is_private`: `BOOLEAN` - Whether or not user profile is visible to other users.
        - `account_status`: `ENUM('active','disabled','suspended','deleted')` - Whether the account is functional or not.
    """

class UserRoles(Base):
    """
    - **User roles** - For assigning privileges based on user status.
        - `id`: `SERIAL PRIMARY KEY`
        - `name`: `TEXT NOT NULL UNIQUE` - Admin, teacher, student, etc.
        - `description`: `TEXT`
    """


# Lakes and Dumps

class AnalyticsRaw(Base):
    __tablename__ = ""
    '''
    - **language-level analytics**
        - `id`: `SERIAL PRIMARY KEY`
        - `word`: `TEXT NOT NULL`
        - `voikko.analyze`: `JSONB`
    '''

class Embeddings(Base):
    __tablename__ = "embeddings"

    content_id = Column(UUID(as_uuid=True), ForeignKey("content.id"), primary_key=True)
    vector = Column(JSONB)
    """
    - **Embeddings**
        - `content_id`: `UUID PRIMARY KEY REFERENCES content(id)` - Unique identifier for each content item.
        - `vector`: `JSONB` - Word or sentence embedding vector.
    """

