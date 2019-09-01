import pandas as pd
import math
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Dense,Dropout

#loading the data
train_variants = pd.read_csv("training_variants.csv")
train_text = pd.read_csv("train_csv.csv")
test_variants = pd.read_csv("test_variants.csv")
test_text = pd.read_csv("test_csv.csv")
#preprocess the data
Text_train = train_text.loc[:,["Text"]]
a = []
for i in Text_train.iterrows():
  index, data = i
  a.append(list(data))
