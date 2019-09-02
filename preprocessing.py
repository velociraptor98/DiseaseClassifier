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
