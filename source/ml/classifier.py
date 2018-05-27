# -*- coding: utf-8 -*-
"""
Created on Sun May 27 15:40:42 2018

@author: aruramam
"""

import pandas as pd
import numpy as np
import os
from datetime import datetime, date, time
import pathlib as pathlib
from sklearn.feature_selection import RFE
from sklearn.svm import SVC
from sklearn.externals import joblib
from sklearn.linear_model import LogisticRegression
from config_model import CONFIG
from loadtrainingdata import _get_training_data_

## get persisted model and data
trainingdata = joblib.load('trainingdata.pkl')
selector_pickle=joblib.load('rfe.pkl')




# get selected features from feature selector
featureselection = selector_pickle.get_support(indices=False)


## Print selected features
print('All features')
print('###################')
print('###################')
for column,series in trainingdata.iteritems():
    print(column)
print('###################')
print('###################')
print('selected features:')

i=0
for column,series in trainingdata.iteritems():
    if (featureselection[i] == True ):
        print(column)
    i+=1

c=[x for x,status in zip(trainingdata.columns.values,featureselection) if status == True ]
print('pickled selector')
training_selected_features = trainingdata.loc[featureselection]
print('treated data list')

##fit data to Logistic regression
regressor = LogisticRegression(C=1.0,fit_intercept = True,solver='liblinear')
startregression = datetime.now()
print("start regression fitting ....")
regressor = regressor.fit(trainingdata[c],y)
endregression = datetime.now()
print('end regression fitting ....')
print('time taken for fitting')
print(endregression - startregression)
print(regressor.coef_)

# =============================================================================
