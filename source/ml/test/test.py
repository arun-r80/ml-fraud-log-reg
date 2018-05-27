# -*- coding: utf-8 -*-
"""
Created on Sun May 27 13:31:24 2018

@author: aruramam
"""

import sys
sys.path.append('..')
from predictor import predict_fraudulent_singleentry
from config_model import CONFIG


print(" Test Case 1 : Gender: Male, Procedure Code 78 is not fradulent")
print(predict_fraudulent_singleentry("Male","NA2"))
if predict_fraudulent_singleentry("Male","NA2") == CONFIG.FRAUD_MAPPING["0.0"]:
    print("Pass")
else:
    print("Fail")
