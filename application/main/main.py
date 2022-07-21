import flask
import random
from urllib import request
from collections import Counter
from flask import Blueprint, render_template
from flask import current_app as app
import re, json
from matplotlib.style import use
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#from wordcloud import WordCloud
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction import DictVectorizer
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score,precision_score,recall_score,confusion_matrix,roc_curve,classification_report
from scikitplot.metrics import plot_confusion_matrix
#from application.api import create_dataframe1
#from application.api import create_dataframe2
#from application.api import create_dataframe3
import pickle
from pprint import pprint
nltk.download()

from nltk.sentiment import SentimentIntensityAnalyzer

vectorizer = DictVectorizer(sparse = True)

def ngram(token, n):
    output = []
    for i in range(n-1, len(token)):
        ngram = ' '.join(token[i-n+1:i+1])
        output.append(ngram)
    return output

def create_feature(text, nrange=(1, 1)):
    text_features = []
    text = text.lower()
    text_alphanum = re.sub('[^a-z0-9#]', ' ', text)
    for n in range(nrange[0], nrange[1]+1):
        text_features += ngram(text_alphanum.split(), n)
    text_punc = re.sub('[a-z0-9]', ' ', text)
    text_features += ngram(text_punc.split(), 1)
    return Counter(text_features)

# Blueprint Configuration
main_bp = Blueprint(
    'main_bp', __name__,
    template_folder='templates',
    static_folder='static'
)

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
    #mainpage.
    if flask.request.method == 'GET':
        # Just render the initial form, to get input
        return(flask.render_template('main.html'))
    
    if flask.request.method == 'POST':
        # Get the input from the user.
        user_input_text = flask.request.form['user_input_text']

        #Created new list to store userinput
        #list1 = re.split('\s+', user_input_text)    
        #print(list1)
        sia = SentimentIntensityAnalyzer
        sia.polarity_scores(user_input_text)
        
        '''username = get_username(list1)
        phrase = get_phrase(list1)
        print(username)
        print(phrase)
        '''
        
        # function to take the input statement and perform the same transformations we did earlier
        def sentiment_predictor(input):
            input = sia.polarity_scores(user_input_text)
            return input

        squell_response = sentiment_predictor(user_input_text)
        return flask.render_template('main.html',
            input_text=user_input_text,
            squell_response = squell_response  
            )