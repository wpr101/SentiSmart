import os
from flask import Flask, render_template, request, redirect, url_for, Response
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
import nltk
#from nltk.book import text7

app = Flask(__name__)

@app.route('/sentiment', methods=['GET'])
def Sentiment():

    return render_template ('sentiment.html')

@app.route('/sentiment-analysis', methods=['POST'])
def SentimentAnalysis():

    user_word = request.form['words']
    word_list = user_word.split()
    count = CountVectorizer()
    docs = np.array([user_word])
    bag = count.fit_transform(docs)
    word_map = count.vocabulary_
    bag_array = bag.toarray()

    tfidf = TfidfTransformer()
    np.set_printoptions(precision=2)
    tfidf_array = tfidf.fit_transform(count.fit_transform(docs)).toarray()

    return render_template ('sentiment-analysis.html', word_list=word_list,
    			    word_map=word_map, bag_array = bag_array, tfidf_array=tfidf_array)
  
	
if __name__ == '__main__':
    #app.run(debug=True, host='0.0.0.0', port=33507)
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
