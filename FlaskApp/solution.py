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

corpus_train=[]
for i in range(3316):
  corpus_train.extend(a[i])

cv = CountVectorizer(max_features = 1200)
X = cv.fit_transform(corpus_train).toarray()
X = pd.DataFrame(X)

#Transforming data
train_variants = train_variants.drop(columns=["ID"])
y_train = train_variants["Class"]
del train_variants["Class"]
train_variants = pd.get_dummies(train_variants,drop_first=True)
train_variants2 = train_variants.join(X,how='outer')

#Transforming test_data
Text_test = test_text.loc[:,["Text"]]
a1 = []
for i in Text_test.iterrows():
    index, data = i
    a1.append(list(data))
  
corpus_test=[]
for i in range(367):
    corpus_test.extend(a1[i])

X_test = cv.transform(corpus_test).toarray()
test_variants = test_variants.drop(columns=["ID"])
y_test = test_variants["Class"]
del test_variants["Class"]
test_variants = pd.get_dummies(test_variants,drop_first=True)
X_test=pd.DataFrame(X_test)
test_variants2 = test_variants.join(X_test,how='outer')

#Gettinng common columns so as to keep number of features same
common_columns = train_variants2.columns.intersection(test_variants2.columns)

#Changing train_variants2
train_columns_remove = train_variants2.columns.difference(common_columns)
train_variants2 = train_variants2.drop(columns=train_columns_remove)

#Changing test_variants2
test_columns_remove = test_variants2.columns.difference(common_columns)
test_variants2 = test_variants2.drop(columns=test_columns_remove)