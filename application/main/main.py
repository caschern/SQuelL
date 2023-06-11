import flask
import random
from urllib import request
from collections import Counter
from flask import Blueprint, render_template
from flask import current_app as app
import re, json
from matplotlib.style import use
from sklearn.feature_extraction import DictVectorizer
from pprint import pprint
#nltk.download()        turn on later
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from .secretwords import fiftyPoints
#from nltk.sentiment import SentimentIntensityAnalyzer

vectorizer = DictVectorizer(sparse = True)

# Blueprint Configuration
main_bp = Blueprint(
    'main_bp', __name__,
    template_folder='templates',
    static_folder='static'
)

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
        return(flask.render_template('main.html'))
    
    if flask.request.method == 'POST':
        # Get the input from the user.
        user_input_text = flask.request.form['user_input_text']

        textTransform = user_input_text.strip('?!.,:;@#$%^&*()-_+=[]') #strip grammatical characters

        textTransform = textTransform.replace(' ','') #strip white spaces
        print(textTransform)

        #User re-enter if numbers are present
        if (str.isalpha(textTransform) == False):
            squell_response = "Letters and words in the sentence only please!"
            
            return flask.render_template('main.html',
            input_text=user_input_text,
            squell_response = squell_response
        )

        #Execute game operations when initial string parsing passes
        elif (str.isalpha(textTransform) == True):
            analyzer = SentimentIntensityAnalyzer()

            parsedText = user_input_text.strip('?!.,:;@#$%^&*()-_+=[]')

            wordArray = parsedText.split(' ')

            print(wordArray)

            phraseScore = 0

            for word in wordArray:
                for c in word:
                    if c.isupper():
                        phraseScore += 2
                    if c.islower():
                        phraseScore += 1
            print(phraseScore)
            
            #check for secret words
            for word in wordArray:
                for index in fiftyPoints:
                    if (word.lower() == index):
                        phraseScore += 50

            #sentiment functions
            def responseBuilder(string):
                polarity = analyzer.polarity_scores(string)
                pos = polarity["pos"]
                neu = polarity["neu"]
                neg = polarity["neg"]
                posScore = round(pos*100,2)
                neuScore = round(neu*100,2)
                negScore = round(neg*100,2)
                return posScore, neuScore, negScore
            def sentiment_predictor(string):
                posScore = responseBuilder(string)[0]
                neuScore = responseBuilder(string)[1]
                negScore = responseBuilder(string)[2]
                print(posScore,neuScore,negScore)
                if (posScore >50 and negScore < 50):
                    response = "Hey, great sentence friend! your sentence score is "
                    return response
                elif (posScore >=0 and neuScore>=50 and negScore >=0):
                    response = "Interesting sentence... your sentence score is "
                    return response
                elif (posScore<50 and negScore > 50):
                    response = "Shocking sentence! your sentence score is "
                    return response
                
            squell_response = sentiment_predictor(user_input_text)
        
        return flask.render_template('main.html',
            phraseScore = phraseScore,
            input_text = user_input_text,
            squell_response = squell_response
        )