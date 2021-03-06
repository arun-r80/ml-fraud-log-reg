# -*- coding: utf-8 -*-
"""
Created on Fri May 25 07:24:03 2018

@author: aruramam
"""
import pandas as pd
from datetime import datetime
from sklearn.feature_selection import RFE
from sklearn.svm import SVC
from sklearn.externals import joblib
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
#selector_pickle=joblib.load('rfe.pkl')
print(selector.get_support(indices=True))
print(selector.get_support(indices=False))
#








