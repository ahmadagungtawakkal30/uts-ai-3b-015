# -*- coding: utf-8 -*-
"""
Created on Sun May  9 08:13:54 2021

@author: ahmad
"""
from flask import Flask, render_template, request
from textblob import TextBlob
import re

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])

def index():
    if request.method == 'POST': 
        url = request.form['url']
        remove = url.replace(('-'),' ')
        change = r"https?://(www\.)?"
        text = re.sub(change, ' ', remove)
        sentimen = TextBlob(text).sentiment
        pol = sentimen.polarity
        sub = sentimen.subjectivity
        #polarity
        if pol < 0:
            analy_pol = "Negative"
        elif pol == 0:
            analy_pol = "Netral"
        else:
            analy_pol = "Positive"
        #subjective
        if sub < 0:
            analy_sub = "Negative"
        elif sub == 0:
            analy_sub = "Netral"
        else:
            analy_sub = "Positive"
        
        return render_template('index.html', url=url, pol=pol, analy_pol=analy_pol, sub=sub, analy_sub=analy_sub)
    return render_template('layout.html')
#if __name__ == "__main__":
#    app.run(debug=True)
