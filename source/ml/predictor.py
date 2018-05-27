# -*- coding: utf-8 -*-
"""
Created on Sun May 27 23:23:03 2018

@author: aruramam
"""


import pandas as pd
from sklearn.externals import joblib
from config_model import CONFIG

#predict correct value with pickeld regressor
def predict_fraudulent_singleentry(gender, primary_procedure_code_no):
    regressor= joblib.load('regressor.pkl')
    ##give test values
    input_dict = {
            'gender':pd.Series([CONFIG.GENDER_MAPPING[gender]]),
            'primary_code':pd.Series([CONFIG.PRIMARY_PROCEDURECODE_MAPPING[primary_procedure_code_no]])
            }
    input=pd.DataFrame(input_dict)
    #predict using regressor
    c=regressor.predict(input)
    return(CONFIG.FRAUD_MAPPING[str(c[0])])
 
#print(predict_fraudulent_singleentry("Male","NA2"))