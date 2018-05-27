# -*- coding: utf-8 -*-
"""
Created on Sun May 27 15:03:26 2018

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

def _get_training_data_():
    #load all configuration files to convert input data to numbers
    #TODO: load other configuration files
    url = os.path.join('ml-config','claim\claimtype.csv')
    claimtype = pd.read_csv(url,delimiter='\s+', header=0)
   
    ##load training data from csv
    url2 = os.path.join('ml-config','trainingdata\\trainingdata_02.csv')
    trainingdata_csv=pd.read_csv(url2,header=0)
    
    
    #convert textual claim fields to numberic fields
    #using configuration files
    #TODO: create fields for other claim detail columns
    df_final=pd.merge(trainingdata_csv,claimtype,on='PendCode',how='left')
    
   
    ##create target row - the row which would be used as "solution" or "result set" for supervvised learning
    df_final['CLAIMREJECTCODENONO'] = np.where( df_final['CLAIMREJECTCODENONO'] * df_final['PROB'] >= CONFIG.THRESHOLD_FRAUD_WEIGHTAGE, np.ones( df_final.shape[0]) , np.zeros( df_final.shape[0]))
    
    ## return the data set
    return df_final

