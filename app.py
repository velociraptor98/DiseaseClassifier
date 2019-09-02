# -*- coding: utf-8 -*-
"""
Created on Sun Sep 01 20:33:05 2019

@author: Spikee
"""

import csv

import predictor

from flask import Flask, render_template, request
app = Flask(__name__)

wCancer={}
wHiv={}

@app.route('/')
def index(methods=['GET', 'POST']):
	
   return render_template('index.html')

@app.route('/inputCancer.html')
def inputCancer():
   return render_template('inputCancer.html')

@app.route('/resultCancer',methods = ['POST', 'GET'])
def resultCancer():
   if request.method == 'POST':
      gene = request.form["Gene"]
      variation=request.form['Variation']
      text=request.form['Text']
      
      wCancer['Gene']= gene
      wCancer['Variation']= variation
      wCancer['Text']= text

      re=predictor.predict(wCancer)
     
      return render_template("resultCancer.html",result = re)
  

@app.route('/inputHIV.html')
def inputHIV():
   return render_template('inputHIV.html')

@app.route('/resultHIV',methods = ['POST', 'GET'])
def resultHIV():
   if request.method == 'POST':
      vl = request.form["VL-t0"]
      cd4=request.form['CD4-t0']

      wHiv["VL-t0"]= v1
      wHiv["CD4-t0"]= cd4

      re=predictorHIV.HIV(wHiv)
      
      return render_template("resultHIV.html",result = re)

 
if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='localhost', port=8080)
    
