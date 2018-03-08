from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object('app.config')

db = SQLAlchemy(app=app)
migrate = Migrate(app=app, db=db)

from app import models
from app import views
