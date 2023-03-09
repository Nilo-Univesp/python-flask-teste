"""
The flask application package.
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from FlaskWebProject1.models import db


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pets.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# initialize the database
db.init_app(app)

# create the database tables
with app.app_context():
    db.create_all()

import FlaskWebProject1.views