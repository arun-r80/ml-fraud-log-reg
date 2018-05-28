# -*- coding: utf-8 -*-
"""
Created on Sun May 27 15:40:42 2018

@author: aruramam
"""

from datetime import datetime
from sklearn.externals import joblib
from sklearn.linear_model import LogisticRegression
from loadtrainingdata import _get_training_data_

## get persisted model and data
trainingdata = joblib.load('trainingdata.pkl')
selector_pickle=joblib.load('rfe.pkl')
# get selected features from feature selector
featureselection = selector_pickle.get_support(indices=False)
c=[x for x,status in zip(trainingdata.columns.values,featureselection) if status == True ]

#get target values for regression
y=_get_training_data_()['CLAIMREJECTCODENONO']

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
print('initiate pickling regressor')
joblib.dump(regressor,'regressor.pkl')
print('regressor picked')

# =============================================================================
