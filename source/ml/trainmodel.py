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


#################################################################3
# =============================================================================
url = os.path.join('ml-config','claim\claimtype.csv')
claimtype = pd.read_csv(url,delimiter='\s+', header=0)
#print(claimtype['PendCode'])
#print(claimtype['PENDCODENO'])
# df = claimtype.loc[claimtype.NO > 1,'PendCode']
#print(df)
# =============================================================================

url2 = os.path.join('ml-config','trainingdata\\trainingdata_01.csv')
#print(url2)
trainingdata_csv=pd.read_csv(url2,header=0)
#print(trainingdata_csv['PendCode'])
#print(trainingdata_csv)
#t3=trainingdata_csv.loc['Pend Code']
#print(t3)
#t2=trainingdata_csv['Pend Code'].apply((lambda x: claimtype.loc[ claimtype.PendCode == x,'NO' ]) )
#print(t2['Pend Code'])
#print(t2)

#merge data with claims
df_final=pd.merge(trainingdata_csv,claimtype,on='PendCode',how='left')
#print(df_final)
#print(df_final.loc[:,'TotalCharge'])
#print(trainingdata_csv['TotalCharge'])
#create training data
#trainingdata = trainingdata_csv.loc[['TotalCharge','Network Indicator','Payee Indicator',
#'Owner Identification','Age','ADMITTINGDIAGNOSISCODENO','MEMBERGENDERNO']]
#trainingdata = trainingdata_csv.loc['TotalCharge']
trainingdata= pd.DataFrame({'TotalCharge':              trainingdata_csv.TotalCharge  ,
                            'Total Benefit Amount':     trainingdata_csv['Total Benefit Amount'],
                           # 'Network Indicator':        trainingdata_csv['Network Indicator'] ,
                          #  'Payee Indicator' :         trainingdata_csv['Payee Indicator'],
                          #  'Owner Identification' :    trainingdata_csv['Owner Identification'] ,
                            'Age':                      trainingdata_csv['Age'],
                         #   'ADMITTINGDIAGNOSISCODENO': trainingdata_csv['ADMITTINGDIAGNOSISCODENO'],
                         #   'PRIMARYDIAGNOSISCODENO':   trainingdata_csv['PRIMARYDIAGNOSISCODENO'],
                            'PRIMARYPROCEDURECODENO':   trainingdata_csv['PRIMARYPROCEDURECODENO'],
                         #   'ADDITIONALPROCEDURETYPE1NO':trainingdata_csv['ADDITIONALPROCEDURETYPE1NO'],
                          #  'BILLINGPROVIDERCODENO':    trainingdata_csv['BILLINGPROVIDERCODENO'],
                            'MEMBERGENDERNO':           trainingdata_csv['MEMBERGENDERNO']
                            
                })

#print(trainingdata)
#we need to create a random fit curvve for the training data set
#so that we can do a feature analysis to get the independent
#we will choose random variables between 0.8-0.9
# =============================================================================
y=trainingdata_csv['CLAIMREJECTCODENONO']
#print(y)
features = ['TotalCharge','Total Benefit Amount','Age','PRIMARYPROCEDURECODENO','MEMBERGENDERNO']
featureselection = [False,True,True,False,False]
i=0
for column,series in trainingdata.iteritems():
    print('In Iteration')
    print(i)
    print(featureselection[i])
    if (featureselection[i] == True ):
        print(column)
    i+=1

# #,'Network Indicator']#,'Payee Indicator','Owner Identification','Age']]
# #print(trainingdata)
estimator = SVC(kernel="linear",C=1)
selector = RFE(estimator,step=1)
starttime=datetime.now()
print('Starting fitting.....')
#selector.fit(trainingdata,y)
print('finised  fitting..........')
endtime=datetime.now()
print('time taken for fitting : ')
print(endtime - starttime)
print('get from pickle')
selector_pickle=joblib.load('rfe.pkl')
print(selector.get_support(indices=True))
print(selector.get_support(indices=False))

#featureselection = selector_pickle.get_support(indices=False)
featureselection = selector.get_support(indices=False)
## Print selected features
print('selected features:')
i=0
for column,series in trainingdata.iteritems():
    
    
    print(featureselection[i])
    if (featureselection[i] == True ):
        print(column)
    i+=1
## pickle the selector 
#joblib.dump(selector,'rfe.pkl')
print('pickled selector')
# =============================================================================








