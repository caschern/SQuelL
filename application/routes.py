"""Core Flask app routes."""
from flask import Flask
from flask_assets import Environment



def create_app():
    """Create Flask application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')
    assets = Environment()  # Create an assets environment
    assets.init_app(app)  # Initialize Flask-Assets
    with app.app_context():
        # Import parts of our application
        from .profile import profile
        from .home import home
        from .products import products
        from .assets import compile_static_assets

        # Register Blueprints
        app.register_blueprint(profile.account_bp)
        app.register_blueprint(home.home_bp)
        app.register_blueprint(products.product_bp)

        # Compile static assets
        compile_static_assets(assets)  # Execute logic

        return app


@app.route('/' method = ['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        # Just render the initial form, to get input
        return(flask.render_template('index.html'))
        #return(flask.render_template('index.html'))
    
    if flask.request.method == 'POST':
        # Get the input from the user.
        
        user_input_text = flask.request.form['user_input_text']
        #Created new list to store userinput
        list1 = re.split('\s+', user_input_text)    
        print(list1)
        j=0
        
        #data_frame = df[df['message_clean'].str.contains(Filter)]
        
        #data_frame = df[x for x in usertext if df['message_clean'].str.contains(x).any()]
        #data_frame = df[df['message_clean'].str.contains(list1[j]) & df['message_clean'].str.contains(list1[j+1]) & df['message_clean'].str.contains(list1[j+2])]
    
        return flask.render_template('index.html', 
            input_text=user_input_text
            )