from flask import Flask
from backend.utils.db_connect import db
from backend.utils.config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    return app