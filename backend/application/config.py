import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.venv'))


class Config:
    CSRF_ENABLED = os.environ.get("CSRF_ENABLED")
    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SESSION_FILE_THRESHOLD = 25
    SESSION_TYPE = 'filesystem'

    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    tracking = os.environ.get("SQLALCHEMY_TRACK_MODIFICATIONS")
    SQLALCHEMY_TRACK_MODIFICATIONS = tracking


class TestingConfig(Config):
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = "sqlite://"


class ProductionConfig(Config):
    Debug = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_PRODUCTION_DB_URI')
