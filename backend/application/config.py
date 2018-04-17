import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.venv'))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    CSRF_ENABLED = os.environ.get("CSRF_ENABLED")

    tracking = os.environ.get("SQLALCHEMY_TRACK_MODIFICATIONS")
    SQLALCHEMY_TRACK_MODIFICATIONS = False or tracking
