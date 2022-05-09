import flask
from flask import Blueprint, render_template
from flask import current_app as app
import re, json
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
from application.api import create_dataframe1
from application.api import create_dataframe2
from application.api import create_dataframe3


# Blueprint Configuration
main_bp = Blueprint(
    'main_bp', __name__,
    template_folder='templates',
    static_folder='static'
)

test = create_dataframe1()
train = create_dataframe2()
val = create_dataframe3()

def sentiResp():
    sigma = 'hi'
    return sigma


def get_username(array):
    username = ''
    for c in array[0]:
        username+=c
    return username
def get_phrase(array):
    phrase = []
    for i in array:
       phrase.append(i)
    phrase.pop(0)
    return phrase
    

@main_bp.route('/', methods=['GET', 'POST'])
def main():
    """mainpage."""
    if flask.request.method == 'GET':
        # Just render the initial form, to get input
        return(flask.render_template('main.html'))
    
    if flask.request.method == 'POST':
        # Get the input from the user.
        user_input_text = flask.request.form['user_input_text']
        #Created new list to store userinput

        list1 = re.split('\s+', user_input_text)    
        print(list1)
        username = get_username(list1)
        phrase = get_phrase(list1)
        print(username)
        print(phrase)

        squell_response = sentiResp()
        
        return flask.render_template('main.html',
            input_text=user_input_text,
            squell_response = squell_response  
            )