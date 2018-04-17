from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from application.config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app=app)
migrate = Migrate(app=app, db=db)

from application import models
from application import views
