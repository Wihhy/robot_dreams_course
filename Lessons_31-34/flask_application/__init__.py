from flask import Flask, request
from logging.config import dictConfig
from config import AppConfig
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)
load_dotenv()

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
})

app.config.from_object(AppConfig)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flask-application.sqlite'

db.init_app(app)

from views import *
from models import *

with app.app_context():
    db.create_all()
