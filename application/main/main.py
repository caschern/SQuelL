from flask import Blueprint, render_template
from flask import current_app as app
import flask
import re, json
from flask import Flask


# Blueprint Configuration
main_bp = Blueprint(
    'main_bp', __name__,
    template_folder='templates',
    static_folder='static'
)


@main_bp.route('/', methods=['GET', 'POST'])
def main():
    """mainpage."""
    products = 'zeta'
    if flask.request.method == 'GET':
        # Just render the initial form, to get input
        return(flask.render_template('main.html'))
    
    if flask.request.method == 'POST':
        # Get the input from the user.
        
        user_input_text = flask.request.form['user_input_text']
        #Created new list to store userinput
        list1 = re.split('\s+', user_input_text)    
        print(list1)
        j=0
        
        return flask.render_template('main.html', 
            input_text=user_input_text
            )