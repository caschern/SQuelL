from flask import Flask
from flask_assets import Environment
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy

import string
db = SQLAlchemy()

def init_app():
    """Construct core Flask application with embedded Dash app."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.Config")
    assets = Environment()
    assets.init_app(app)
    db.init_app(app)


    with app.app_context():
        # Import parts of our application
        from .main import main
        from . import routes
        from .assets import compile_static_assets

        # Register Blueprints
        app.register_blueprint(main.main_bp)
        compile_static_assets(assets)
        db.create_all() #create sql tables for our data models

        return app