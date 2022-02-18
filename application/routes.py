"""Core Flask app routes."""
from flask import Flask
from flask_assets import Environment
import os 
from flask import send_from_directory  
"""Routes for main pages."""
from flask import Blueprint


main_bp = Blueprint(
    'main_bp',
    __name__,
    template_folder='templates',
    static_folder='static'
)


def create_app():
    """Create Flask application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')
    assets = Environment()  # Create an assets environment
    assets.init_app(app)  # Initialize Flask-Assets
    with app.app_context():
        # Import parts of our application
        # from .profile import profile
        from .main import main
        from .assets import compile_static_assets

        # Register Blueprints
        # app.register_blueprint(profile.account_bp)
        app.register_blueprint(main.main_bp)

        # Compile static assets
        compile_static_assets(assets)  # Execute logic

        return app