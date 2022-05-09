"""Core Flask app routes."""
from flask import Flask
from flask_assets import Environment
import os 
from flask import send_from_directory  
"""Routes for main pages."""
from flask import Blueprint
from flask import request, render_template, make_response
from datetime import datetime as dt
from flask import current_app as app
from application.models import db, User

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


def user_records(array):
    left=[]
    right=[]
    for i in array:
        while i != ',':
            left.append(i)
    for i in range(len(left), len(array)-1):
        right.append(i)
    for i in right:
        print(i)

'''
    username = request.args.get('user')
    phrase = request.args.get('phrase')
    if username and phrase:
        new_user = User(
            username = username,
            phrase = phrase,
            created=dt.now(),
            admin=False
        )
        db.session.add(new_user)  # Adds new User record to database
        db.session.commit()
    return make_response(f"{new_user} successfully created!")       # Commits all changes'''