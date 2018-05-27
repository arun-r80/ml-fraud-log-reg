# -*- coding: utf-8 -*-
"""
Created on Sun May 27 19:41:11 2018

@author: aruramam
"""
from sklearn.externals import joblib

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

