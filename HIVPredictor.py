# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 22:34:48 2019

@author: Shivam-PC
"""

# importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#importing training dataset
dataset_training = pd.read_csv("training_data.csv")
X_train = dataset_training.iloc[:, [4,5]].values #VL-t0 and CD4-t0 values
y_train = dataset_training.iloc[:, 1].values #target values

#spitting the dataset into training set and text set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split( X_train , y_train, test_size=0.2, random_state=0)

# Fitting Logistic regression to training set
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state = 0)
classifier.fit(X_train, y_train)

# predicting the results
y_pred = classifier.predict(X_test)

# Making the confusion Matrix
from sklearn.metrics import confusion_matrix
confusionMatrix = confusion_matrix(y_test, y_pred)
print(confusionMatrix)

# 78% accuracy reached
print(classifier.score(X_test,y_test))
