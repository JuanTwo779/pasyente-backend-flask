# Creation of app instance

from flask import Flask
from src.extensions import db, migrate
from src.config import Config

def create_app():
     app = Flask(__name__)

     # config
     app.config.from_object(Config)

     # extensinos
     db.init_app(app)
     migrate.init_app(app, db)

     # register blueprints
     from src.routes import register_blueprints
     register_blueprints(app)

     return app