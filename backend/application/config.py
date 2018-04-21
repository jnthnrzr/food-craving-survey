import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.venv'))


class Config:
    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SESSION_TYPE = 'filesystem'
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    CSRF_ENABLED = os.environ.get("CSRF_ENABLED")

    tracking = os.environ.get("SQLALCHEMY_TRACK_MODIFICATIONS")
    SQLALCHEMY_TRACK_MODIFICATIONS = tracking


class TestingConfig(Config):
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = "sqlite://"
