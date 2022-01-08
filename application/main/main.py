import flask
from flask import Blueprint, render_template
from flask import current_app as app
import re, json
from flask import Flask
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score,precision_score,recall_score,confusion_matrix,roc_curve,classification_report
from scikitplot.metrics import plot_confusion_matrix


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
        squell_response = "so you've arrived..."
        
        return flask.render_template('main.html', 
            input_text=user_input_text,
            squell_response = squell_response
            )