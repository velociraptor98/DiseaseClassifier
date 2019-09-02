# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 09:54:15 2019

@author: Shivam-PC

File for predicting using the saved HIV Progression model
"""

import pickle
import pandas as pd
def HIV(a, b):
    classifier = pickle.load(open("HIVProgression.sav", 'rb'))
    di = {"VL-t0":[a], "CD4-t0":[b]}
    data = pd.DataFrame(di)  
    print(data)
    result = classifier.predict(data)
    return result
