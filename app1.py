# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 23:33:05 2018

@author: Spikee
"""

from flask import Flask, render_template, request
app = Flask(__name__)


def call(gene,var,text):
    st=gene+var+text
    return st

@app.route('/')
def student():
   return render_template('Input.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      gene = request.form["Gene"]
      variation=request.form['Variation']
      text=request.form['Text']
      
      re=call(gene,variation,text)
      
      return render_template("result.html",result = re)

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='localhost', port=8080)
    
