from backend.app.models import Languages, LanguagePhrases, LanguageSigns, LanguageWords
from backend.app.services.database import get_db


def get_all_languages():
    db = get_db()
    languages = db.query(Languages).all()
    return languages


def get_language_by_id(language_id):
    db = get_db()
    language = db.query(Languages).filter_by(id=language_id).first()
    return language


def get_phrases_in_language(language_id):
    db = get_db()
    phrases = db.query(LanguagePhrases).filter_by(language_id=language_id).all()
    return phrases


def get_words_in_language(language_id):
    db = get_db()
    words = db.query(LanguageWords).filter_by(language_id=language_id).all()
    return words


def get_signs_in_language(language_id):
    db = get_db()
    signs = db.query(LanguageSigns).filter_by(language_id=language_id).all()
    return signs
