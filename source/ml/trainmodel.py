# -*- coding: utf-8 -*-
"""
Created on Fri May 25 07:24:03 2018

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


#################################################################
#################################################################
#################################################################
#Get treated training data as dataframe 
trainingdata_load = _get_training_data_();
#Get feature candidates from training data
#No of features have been limited to just five, for experimental purposes
trainingdata= pd.DataFrame({'TotalCharge':              trainingdata_load.TotalCharge  ,
                            'Total Benefit Amount':     trainingdata_load['Total Benefit Amount'],
#                           'Network Indicator':        trainingdata_load['Network Indicator'] ,
#                           'Payee Indicator' :         trainingdata_load['Payee Indicator'],
#                           'Owner Identification' :    trainingdata_load['Owner Identification'] ,
                            'Age':                      trainingdata_load['Age'],
#                           'ADMITTINGDIAGNOSISCODENO': trainingdata_load['ADMITTINGDIAGNOSISCODENO'],
#                           'PRIMARYDIAGNOSISCODENO':   trainingdata_load['PRIMARYDIAGNOSISCODENO'],
                            'PRIMARYPROCEDURECODENO':   trainingdata_load['PRIMARYPROCEDURECODENO'],
#                           'ADDITIONALPROCEDURETYPE1NO':trainingdata_load['ADDITIONALPROCEDURETYPE1NO'],
#                           'BILLINGPROVIDERCODENO':    trainingdata_load['BILLINGPROVIDERCODENO'],
                            'MEMBERGENDERNO':           trainingdata_load['MEMBERGENDERNO']
                            
                })

#we need to create a random fit curvve for the training data set
#so that we can do a feature analysis to get the independent
#variables.
# =============================================================================
y=trainingdata_load['CLAIMREJECTCODENONO']

features = ['TotalCharge','Total Benefit Amount','Age','PRIMARYPROCEDURECODENO','MEMBERGENDERNO']
featureselection = [False,True,True,False,False]



##FEATURE ANALYSIS##############

#Algorithm used : Recursive Feature elimination
#Estimator for RFE : Support Vector Classification
estimator = SVC(kernel="linear",C=1)
selector = RFE(estimator,step=1)
#start feature analysis
starttime=datetime.now()
print('Starting fitting.....')
selector.fit(trainingdata,y)
print('finised  fitting..........')
endtime=datetime.now()
print('time taken for fitting : ')
print(endtime - starttime)
#persist feature selection model -"Pickle it"
#Also, store training data to use later
print('Pickling the model')
joblib.dump(selector,'rfe.pkl')
joblib.dump(trainingdata,'trainingdata.pkl')
print('training data pickled')
selector_pickle=joblib.load('rfe.pkl')
print(selector.get_support(indices=True))
print(selector.get_support(indices=False))

featureselection = selector_pickle.get_support(indices=False)
print(featureselection)
#featureselection = selector.get_support(indices=False)
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
## pickle the selector 
#joblib.dump(selector,'rfe.pkl')
c=[x for x,status in zip(trainingdata.columns.values,featureselection) if status == True ]
print('pickled selector')
training_selected_features = trainingdata.loc[featureselection]
print('treated data list')
print(trainingdata[c])
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








