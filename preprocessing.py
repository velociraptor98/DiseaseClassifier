# importing python libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv
import nltk
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
import string
from nltk.stem import WordNetLemmatizer

# Importing the dataset
file = open('training_text', 'r', encoding='utf-8') 
training_text = file.read()
train_list = training_text.split('\n')
train_list = train_list[1:len(train_list)]

train_csv=csv.writer(open('train_csv.csv','w',encoding = 'UTF-8')) # Inorder to convert all chacarters to UTF-8 standard
train_csv.writerow(['ID','Text'])

stopwords = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def text_process(sent):
   all_words=[]
   sent=sent.translate(str.maketrans("","",string.punctuation))
   tokenized=word_tokenize(sent)
   for w in tokenized:
       word=w.lower()
       if word.isalpha() and word not in stopwords:
           word=lemmatizer.lemmatize(word)
           all_words.append(word)
   str1=" ".join(all_words)
   return str1

for i in range(0,3321):
    lable,text = train_list[i].split('||')
    text = text_process(text)
    train_csv.writerow([lable,text])
    
file2 = open('test_text', 'r', encoding='utf-8') 
test_text = file2.read()
test_list = test_text.split('\n')
X_test =[]
y_test=[]

test_csv=csv.writer(open('test_csv.csv','w',encoding = 'UTF-8'))
test_csv.writerow(['ID','Text'])

for i in range(0,368):
    lable,text = test_list[i].split('||')
    text = text_process(text)
    test_csv.writerow([lable,text])
       
    
    
