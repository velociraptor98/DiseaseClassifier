# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 22:34:48 2019

@author: Shivam-PC

Appling Machine Learning on HIV progression dataset predict 
the likelihood that an HIV patient's infection will become less severe.
"""

# importing libraries
import pandas as pd
import pickle

#importing training dataset
dataset_training = pd.read_csv("HIV_training_data.csv")
#VL-t0 and CD4-t0 values
X_train = dataset_training.iloc[:, [4,5]].values 
#target values in binary 1/0  
y_train = dataset_training.iloc[:, 1].values 

#scaling CD4-t0 training values 
X_train[:,1]=X_train[:,1]/100

#spitting the dataset into training set and text set test size=0.10
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split( X_train , y_train, test_size=0.10, random_state=0)

#scaling VL-t0 testing values 
X_test[:,1]=X_test[:,1]/100

# Fitting Logistic regression to training set
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state = 0)
classifier.fit(X_train, y_train)

# predicting the results
y_pred = classifier.predict(X_test)

# Making the confusion Matrix
from sklearn.metrics import confusion_matrix
confusionMatrix = confusion_matrix(y_test, y_pred)
print('Confusion Matrix : ')
print(confusionMatrix)

# 84% accuracy reached by increasing test data
print('score :',classifier.score(X_test,y_test))

#Saving the classifier to file HIVProgression

with open('HIVProgression.sav', 'wb') as HIVFile:
    pickle.dump(classifier, HIVFile)

#testing the saved classifier
classifierLoad = pickle.load(open("HIVProgression.sav", 'rb'))
result = classifierLoad.predict(X_test)

print('score :',classifierLoad.score(X_test,y_test))

