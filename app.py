# -*- coding: utf-8 -*-
"""
Created on Sun Sep 01 20:33:05 2019

@author: Spikee
"""

import csv

import predictor

from flask import Flask, render_template, request
app = Flask(__name__)

writer={}



@app.route('/')
def student():
   return render_template('Input.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      gene = request.form["Gene"]
      variation=request.form['Variation']
      text=request.form['Text']
      
      writer['Gene']= gene
      writer['Variation']= variation
      writer['Text']= text

      re=predictor.predict(writer)
      
      return render_template("result.html",result = re)

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='localhost', port=8080)
    
