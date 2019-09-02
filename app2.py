# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 23:33:05 2018

@author: Spikee
"""

import csv
import predictor
import predictorHIV


from flask import Flask, render_template, request
app = Flask(__name__)

fCancer=open("sample1.csv","w",encoding="utf-8")
wCancer=csv.writer(fCancer)
wCancer.writerow(['Gene','Variation','Text'])


fHiv=open("sample2.csv","a+",encoding="utf-8")
wHiv=csv.writer(fHiv)
#wHiv.writerow(['VL-t0','CD4-t0'])


@app.route('/')
def index():
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
      
      wCancer.writerow([gene,variation,text])
      re=predictor.predict()
     
      return render_template("resultCancer.html",result = re)
  
    
    

@app.route('/inputHIV.html')
def inputHIV():
   return render_template('inputHIV.html')

@app.route('/resultHIV',methods = ['POST', 'GET'])
def resultHIV():
   if request.method == 'POST':
      vl = request.form["VL-t0"]
      cd4=request.form['CD4-t0']
      #wHiv.writerow([vl,cd4])
      
      re=predictorHIV.HIV(vl,cd4)
      
      return render_template("resultHIV.html",result = re)

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='localhost', port=8080)
    
