# -*- coding: utf-8 -*-
"""
Created on Sun May 27 13:31:24 2018

@author: aruramam
"""

import sys
sys.path.append('..')
from predictor import predict_fraudulent_singleentry
from config_model import CONFIG


print("Positive Test Case 1 : Gender: Male, Procedure Code 78 is not fradulent")

if predict_fraudulent_singleentry("Male","NA1") == CONFIG.FRAUD_MAPPING["0.0"]:
    print("Pass")
else:
    print("Fail")
    
print("Negative Test Case 1 : Gender: Male, Procedure Code 78 is not fradulent")

if predict_fraudulent_singleentry("Male","MYP") == CONFIG.FRAUD_MAPPING["1.0"]:
    print("Pass")
else:
    print("Fail")
       
    
for i in CONFIG.GENDER_MAPPING:
    for j in CONFIG.PRIMARY_PROCEDURECODE_MAPPING:
        c =  predict_fraudulent_singleentry(i,j)
        print('Gender Mapping :',i, ' Primary Procedure code: ',j,'Validation status :',c)
